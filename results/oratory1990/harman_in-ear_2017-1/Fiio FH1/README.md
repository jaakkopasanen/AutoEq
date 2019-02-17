# Fiio FH1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -14.4; 25 -14.6; 28 -14.3; 31 -14.2; 34 -14.2; 37 -14.1; 41 -14.2; 45 -14.1; 49 -14.1; 54 -14.4; 60 -14.4; 66 -14.8; 72 -14.7; 79 -14.9; 87 -15.0; 96 -14.5; 106 -14.8; 116 -14.4; 128 -14.4; 141 -14.1; 155 -13.8; 170 -13.6; 187 -13.3; 206 -13.0; 227 -12.5; 249 -12.1; 274 -11.7; 302 -11.1; 332 -10.5; 365 -10.0; 402 -9.4; 442 -8.9; 486 -8.4; 535 -7.9; 588 -7.4; 647 -6.9; 712 -6.5; 783 -6.0; 861 -5.9; 947 -6.1; 1042 -6.8; 1146 -7.8; 1261 -8.7; 1387 -9.2; 1526 -9.4; 1678 -9.5; 1846 -9.5; 2031 -8.9; 2234 -7.6; 2457 -5.7; 2703 -4.1; 2973 -3.1; 3270 -2.8; 3597 -2.1; 3957 -0.5; 4353 -0.5; 4788 -3.4; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.5; 8482 -10.5; 9330 -10.2; 10263 -7.7; 11289 -6.5; 12418 -6.6; 13660 -11.7; 15026 -19.9; 16529 -24.6; 18182 -24.7; 20000 -23.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.22 | -8.6 dB  |
| Peaking | 5036 Hz  | 0.72 | 16.2 dB  |
| Peaking | 12607 Hz | 0.99 | 21.8 dB  |
| Peaking | 15400 Hz | 0.21 | -28.2 dB |
| Peaking | 20824 Hz | 1.62 | -5.0 dB  |
| Peaking | 848 Hz   | 1.65 | 2.9 dB   |
| Peaking | 1821 Hz  | 1.03 | -4.7 dB  |
| Peaking | 3337 Hz  | 0.86 | 6.1 dB   |
| Peaking | 5403 Hz  | 1.19 | -7.7 dB  |
| Peaking | 6207 Hz  | 3    | 7.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -20.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Fiio%20FH1/Fiio%20FH1.png)