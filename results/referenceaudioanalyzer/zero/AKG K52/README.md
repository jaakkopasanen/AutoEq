# AKG K52
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.8; 25 -14.3; 28 -14.9; 31 -15.3; 34 -15.6; 37 -15.6; 41 -15.4; 45 -15.2; 49 -15.0; 54 -14.8; 60 -14.3; 66 -13.6; 72 -12.9; 79 -12.1; 87 -11.6; 96 -12.1; 106 -13.0; 116 -13.3; 128 -13.5; 141 -13.9; 155 -14.0; 170 -13.8; 187 -13.2; 206 -12.4; 227 -11.3; 249 -10.1; 274 -9.1; 302 -8.3; 332 -7.5; 365 -7.3; 402 -8.3; 442 -8.8; 486 -8.6; 535 -7.7; 588 -6.9; 647 -6.4; 712 -5.6; 783 -4.2; 861 -3.6; 947 -3.9; 1042 -3.4; 1146 -2.0; 1261 -0.6; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.8; 3957 -7.3; 4353 -9.6; 4788 -10.0; 5267 -10.0; 5793 -12.1; 6373 -14.6; 7010 -13.3; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K52 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K52 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.55 | -9.0 dB  |
| Peaking | 163 Hz  | 1.22 | -6.4 dB  |
| Peaking | 526 Hz  | 1.64 | -3.0 dB  |
| Peaking | 3193 Hz | 0.32 | 9.5 dB   |
| Peaking | 5771 Hz | 1.09 | -14.6 dB |
| Peaking | 3360 Hz | 4.4  | 3.4 dB   |
| Peaking | 4162 Hz | 3.04 | -4.0 dB  |
| Peaking | 5466 Hz | 4.28 | 3.8 dB   |
| Peaking | 6797 Hz | 3.8  | -4.3 dB  |
| Peaking | 7912 Hz | 4.1  | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K52/AKG%20K52.png)