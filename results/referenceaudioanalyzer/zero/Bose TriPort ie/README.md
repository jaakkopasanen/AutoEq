# Bose TriPort ie
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.8; 23 -14.5; 25 -15.1; 28 -15.9; 31 -16.4; 34 -16.8; 37 -17.1; 41 -17.4; 45 -17.6; 49 -17.7; 54 -17.8; 60 -17.8; 66 -17.8; 72 -17.8; 79 -18.0; 87 -18.1; 96 -18.1; 106 -18.1; 116 -18.0; 128 -17.8; 141 -17.7; 155 -17.4; 170 -17.2; 187 -16.9; 206 -16.6; 227 -16.3; 249 -15.9; 274 -15.5; 302 -15.0; 332 -14.4; 365 -13.9; 402 -13.6; 442 -13.3; 486 -12.9; 535 -12.4; 588 -11.9; 647 -11.4; 712 -10.6; 783 -9.5; 861 -8.2; 947 -6.6; 1042 -4.8; 1146 -2.9; 1261 -0.9; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.7; 2703 -1.2; 2973 -1.3; 3270 -2.6; 3597 -4.6; 3957 -5.5; 4353 -4.2; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose TriPort ie GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose TriPort ie ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.3  | -7.2 dB |
| Peaking | 269 Hz  | 0.19 | -8.5 dB |
| Peaking | 1590 Hz | 0.75 | 10.6 dB |
| Peaking | 5677 Hz | 3.13 | 5.8 dB  |
| Peaking | 1267 Hz | 2.73 | 3.4 dB  |
| Peaking | 1478 Hz | 1.04 | -3.0 dB |
| Peaking | 3306 Hz | 0.88 | 3.0 dB  |
| Peaking | 3868 Hz | 3.51 | -4.5 dB |
| Peaking | 8371 Hz | 2.14 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.3 dB |
| Peaking | 62 Hz    | 1.41 | -8.6 dB |
| Peaking | 125 Hz   | 1.41 | -9.1 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB |
| Peaking | 500 Hz   | 1.41 | -6.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Bose%20TriPort%20ie/Bose%20TriPort%20ie.png)