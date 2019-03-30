# Stax SR-303
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -2.9; 60 -6.4; 66 -9.6; 72 -12.1; 79 -13.7; 87 -13.9; 96 -13.1; 106 -11.7; 116 -10.1; 128 -8.6; 141 -7.5; 155 -6.8; 170 -6.2; 187 -5.8; 206 -5.5; 227 -5.1; 249 -4.7; 274 -4.5; 302 -4.5; 332 -4.5; 365 -4.5; 402 -4.5; 442 -4.4; 486 -4.2; 535 -4.2; 588 -4.5; 647 -4.5; 712 -4.5; 783 -4.7; 861 -5.1; 947 -5.6; 1042 -6.0; 1146 -6.3; 1261 -6.8; 1387 -7.6; 1526 -8.1; 1678 -8.4; 1846 -8.4; 2031 -8.0; 2234 -7.3; 2457 -6.1; 2703 -4.2; 2973 -2.6; 3270 -1.9; 3597 -3.5; 3957 -6.3; 4353 -8.1; 4788 -9.0; 5267 -9.0; 5793 -9.6; 6373 -10.7; 7010 -11.1; 7711 -10.3; 8482 -9.0; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-303 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-303 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 45 Hz   | 0.51 | 10.6 dB  |
| Peaking | 82 Hz   | 1.23 | -15.5 dB |
| Peaking | 354 Hz  | 0.68 | 2.5 dB   |
| Peaking | 3234 Hz | 4.28 | 6.0 dB   |
| Peaking | 6439 Hz | 1.4  | -4.5 dB  |
| Peaking | 768 Hz  | 2.22 | 1.1 dB   |
| Peaking | 1757 Hz | 1.64 | -2.4 dB  |
| Peaking | 2734 Hz | 5.72 | 1.8 dB   |
| Peaking | 7927 Hz | 2.66 | -2.1 dB  |
| Peaking | 8979 Hz | 1.21 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 9.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Stax%20SR-303/Stax%20SR-303.png)