# Audeze Sine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.1; 25 -1.1; 28 -1.3; 31 -1.4; 34 -1.4; 37 -1.4; 41 -1.6; 45 -1.8; 49 -2.0; 54 -2.3; 60 -2.8; 66 -3.2; 72 -3.5; 79 -3.7; 87 -4.1; 96 -4.7; 106 -5.1; 116 -5.5; 128 -5.8; 141 -6.0; 155 -6.3; 170 -6.3; 187 -6.1; 206 -5.9; 227 -6.3; 249 -6.6; 274 -6.9; 302 -6.9; 332 -6.8; 365 -6.6; 402 -6.6; 442 -6.9; 486 -7.1; 535 -6.9; 588 -6.8; 647 -6.6; 712 -6.5; 783 -6.5; 861 -6.6; 947 -6.9; 1042 -7.1; 1146 -7.4; 1261 -7.5; 1387 -7.6; 1526 -7.2; 1678 -7.1; 1846 -7.4; 2031 -7.5; 2234 -7.1; 2457 -6.2; 2703 -6.5; 2973 -6.7; 3270 -6.9; 3597 -7.0; 3957 -5.3; 4353 -3.1; 4788 -2.3; 5267 -2.1; 5793 -1.2; 6373 -0.5; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.7; 10263 -10.6; 11289 -12.8; 12418 -13.4; 13660 -18.5; 15026 -26.0; 16529 -30.9; 18182 -30.4; 20000 -25.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.98 | 4.3 dB   |
| Peaking | 51 Hz    | 1.41 | 2.5 dB   |
| Peaking | 2487 Hz  | 0.3  | -9.0 dB  |
| Peaking | 6566 Hz  | 0.31 | 24.0 dB  |
| Peaking | 16991 Hz | 0.28 | -34.6 dB |
| Peaking | 3544 Hz  | 3.23 | -2.9 dB  |
| Peaking | 4543 Hz  | 0.73 | 1.3 dB   |
| Peaking | 7553 Hz  | 6.6  | -2.8 dB  |
| Peaking | 12732 Hz | 5.87 | 2.6 dB   |
| Peaking | 15114 Hz | 4.22 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB   |
| Peaking | 62 Hz    | 1.41 | 2.2 dB   |
| Peaking | 125 Hz   | 1.41 | -0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 9.4 dB   |
| Peaking | 16000 Hz | 1.41 | -35.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Audeze%20Sine/Audeze%20Sine.png)