# MEE audio M6 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.2; 28 -5.5; 31 -5.7; 34 -5.8; 37 -5.9; 41 -6.0; 45 -6.2; 49 -6.2; 54 -6.3; 60 -6.4; 66 -6.5; 72 -6.7; 79 -6.8; 87 -6.9; 96 -7.0; 106 -7.1; 116 -7.1; 128 -7.0; 141 -6.9; 155 -6.6; 170 -6.4; 187 -6.1; 206 -5.8; 227 -5.4; 249 -5.1; 274 -4.7; 302 -4.2; 332 -3.7; 365 -3.2; 402 -2.8; 442 -2.5; 486 -2.1; 535 -1.5; 588 -1.1; 647 -0.8; 712 -0.6; 783 -0.5; 861 -0.9; 947 -1.5; 1042 -2.3; 1146 -3.4; 1261 -3.8; 1387 -4.3; 1526 -4.9; 1678 -5.7; 1846 -6.7; 2031 -7.8; 2234 -8.7; 2457 -9.6; 2703 -10.8; 2973 -10.8; 3270 -9.7; 3597 -9.2; 3957 -9.8; 4353 -12.3; 4788 -16.2; 5267 -17.0; 5793 -10.3; 6373 -5.5; 7010 -4.9; 7711 -7.0; 8482 -6.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.46 | 1.3 dB   |
| Peaking | 116 Hz  | 0.82 | -1.5 dB  |
| Peaking | 699 Hz  | 0.74 | 5.5 dB   |
| Peaking | 2717 Hz | 1.58 | -5.2 dB  |
| Peaking | 5009 Hz | 4.68 | -12.0 dB |
| Peaking | 5477 Hz | 8.82 | -2.3 dB  |
| Peaking | 6533 Hz | 5.52 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | -7.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M6%20PRO/MEE%20audio%20M6%20PRO.png)