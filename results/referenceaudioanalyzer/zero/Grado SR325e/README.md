# Grado SR325e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.2; 49 -1.9; 54 -2.8; 60 -3.8; 66 -4.5; 72 -5.0; 79 -5.3; 87 -5.4; 96 -5.4; 106 -5.4; 116 -5.2; 128 -5.0; 141 -4.7; 155 -4.4; 170 -4.2; 187 -4.0; 206 -3.7; 227 -3.5; 249 -3.5; 274 -3.4; 302 -3.2; 332 -3.2; 365 -3.1; 402 -2.9; 442 -3.1; 486 -3.7; 535 -3.8; 588 -3.8; 647 -3.8; 712 -3.8; 783 -3.8; 861 -3.8; 947 -3.8; 1042 -4.1; 1146 -4.4; 1261 -4.7; 1387 -5.1; 1526 -5.9; 1678 -7.7; 1846 -10.2; 2031 -12.0; 2234 -12.5; 2457 -11.9; 2703 -10.9; 2973 -9.5; 3270 -7.6; 3597 -7.3; 3957 -10.0; 4353 -12.7; 4788 -13.4; 5267 -13.6; 5793 -13.2; 6373 -11.6; 7010 -9.3; 7711 -6.7; 8482 -6.5; 9330 -8.2; 10263 -11.4; 11289 -12.6; 12418 -12.0; 13660 -9.9; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.91 | 6.7 dB   |
| Peaking | 1936 Hz  | 0.09 | 3.8 dB   |
| Peaking | 2210 Hz  | 1.82 | -9.3 dB  |
| Peaking | 5210 Hz  | 1.74 | -10.4 dB |
| Peaking | 11719 Hz | 1.77 | -8.6 dB  |
| Peaking | 91 Hz    | 2.66 | -0.9 dB  |
| Peaking | 3541 Hz  | 7.32 | 2.0 dB   |
| Peaking | 4250 Hz  | 9.02 | -1.6 dB  |
| Peaking | 8331 Hz  | 3.38 | 4.2 dB   |
| Peaking | 8356 Hz  | 1.6  | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR325e/Grado%20SR325e.png)