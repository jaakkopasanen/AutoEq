# MEE audio M6 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.2; 31 -1.4; 34 -1.6; 37 -1.7; 41 -1.8; 45 -1.8; 49 -1.9; 54 -2.1; 60 -2.6; 66 -2.9; 72 -3.2; 79 -3.6; 87 -4.0; 96 -4.4; 106 -5.0; 116 -5.4; 128 -5.8; 141 -6.1; 155 -6.3; 170 -6.3; 187 -6.3; 206 -6.1; 227 -5.9; 249 -5.7; 274 -5.3; 302 -4.9; 332 -4.3; 365 -3.8; 402 -3.4; 442 -3.1; 486 -2.7; 535 -2.1; 588 -1.6; 647 -1.3; 712 -1.1; 783 -1.0; 861 -1.4; 947 -2.1; 1042 -2.7; 1146 -3.8; 1261 -4.3; 1387 -4.7; 1526 -5.3; 1678 -6.1; 1846 -7.0; 2031 -7.9; 2234 -8.4; 2457 -9.2; 2703 -10.9; 2973 -11.4; 3270 -10.5; 3597 -10.1; 3957 -10.8; 4353 -13.2; 4788 -16.3; 5267 -17.6; 5793 -11.0; 6373 -7.1; 7010 -5.4; 7711 -6.8; 8482 -7.9; 9330 -6.3; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.82 | 5.3 dB   |
| Peaking | 56 Hz   | 1.36 | 2.8 dB   |
| Peaking | 724 Hz  | 0.94 | 5.5 dB   |
| Peaking | 2886 Hz | 1.61 | -4.8 dB  |
| Peaking | 5022 Hz | 4.25 | -11.6 dB |
| Peaking | 94 Hz   | 2.03 | 1.0 dB   |
| Peaking | 159 Hz  | 0.78 | -1.0 dB  |
| Peaking | 370 Hz  | 2.41 | 0.8 dB   |
| Peaking | 6394 Hz | 1.67 | -1.7 dB  |
| Peaking | 6753 Hz | 4.07 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -7.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M6%20PRO/MEE%20audio%20M6%20PRO.png)