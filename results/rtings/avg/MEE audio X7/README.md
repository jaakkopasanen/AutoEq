# MEE audio X7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.6; 31 -2.1; 34 -2.6; 37 -2.9; 41 -3.4; 45 -3.7; 49 -4.1; 54 -4.5; 60 -5.2; 66 -5.9; 72 -6.4; 79 -6.9; 87 -7.4; 96 -8.1; 106 -8.8; 116 -9.4; 128 -10.0; 141 -10.4; 155 -10.6; 170 -10.7; 187 -10.8; 206 -10.9; 227 -10.7; 249 -10.4; 274 -10.0; 302 -9.5; 332 -9.0; 365 -8.4; 402 -7.9; 442 -7.5; 486 -6.9; 535 -6.2; 588 -6.0; 647 -5.8; 712 -5.4; 783 -5.3; 861 -5.6; 947 -6.2; 1042 -6.6; 1146 -7.1; 1261 -7.5; 1387 -7.7; 1526 -8.0; 1678 -8.4; 1846 -9.0; 2031 -9.5; 2234 -9.7; 2457 -10.1; 2703 -11.9; 2973 -14.5; 3270 -16.3; 3597 -17.1; 3957 -18.3; 4353 -21.2; 4788 -21.9; 5267 -15.8; 5793 -10.2; 6373 -7.9; 7010 -7.1; 7711 -8.7; 8482 -9.9; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.3; 15026 -12.5; 16529 -12.1; 18182 -14.0; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.55 | 6.0 dB   |
| Peaking | 174 Hz   | 0.88 | -5.0 dB  |
| Peaking | 4208 Hz  | 1.78 | -15.1 dB |
| Peaking | 14768 Hz | 3.69 | -4.7 dB  |
| Peaking | 18782 Hz | 0.97 | -8.4 dB  |
| Peaking | 753 Hz   | 1.05 | 3.1 dB   |
| Peaking | 1240 Hz  | 0.26 | -1.5 dB  |
| Peaking | 4070 Hz  | 7.37 | 4.2 dB   |
| Peaking | 4799 Hz  | 5.04 | -4.9 dB  |
| Peaking | 6254 Hz  | 2.81 | 4.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.8 dB   |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -14.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -7.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20X7/MEE%20audio%20X7.png)