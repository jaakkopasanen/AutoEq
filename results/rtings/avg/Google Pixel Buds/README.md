# Google Pixel Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.0; 49 -2.3; 54 -4.0; 60 -5.6; 66 -6.9; 72 -7.9; 79 -8.9; 87 -9.9; 96 -10.8; 106 -11.6; 116 -12.3; 128 -12.8; 141 -13.1; 155 -13.3; 170 -13.3; 187 -13.2; 206 -13.0; 227 -12.7; 249 -12.3; 274 -11.8; 302 -11.2; 332 -10.5; 365 -9.9; 402 -9.6; 442 -9.5; 486 -9.4; 535 -9.3; 588 -9.2; 647 -8.9; 712 -8.5; 783 -8.1; 861 -7.5; 947 -6.9; 1042 -6.2; 1146 -5.3; 1261 -4.3; 1387 -3.5; 1526 -2.8; 1678 -2.3; 1846 -2.2; 2031 -2.4; 2234 -2.9; 2457 -4.5; 2703 -6.4; 2973 -8.4; 3270 -9.6; 3597 -10.1; 3957 -10.0; 4353 -9.8; 4788 -9.5; 5267 -9.9; 5793 -9.0; 6373 -7.6; 7010 -6.4; 7711 -8.1; 8482 -9.3; 9330 -7.1; 10263 -6.5; 11289 -6.8; 12418 -10.4; 13660 -11.8; 15026 -11.6; 16529 -11.1; 18182 -10.8; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Google Pixel Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Google Pixel Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.49 | 12.1 dB  |
| Peaking | 109 Hz   | 0.35 | -10.6 dB |
| Peaking | 1910 Hz  | 1.27 | 6.2 dB   |
| Peaking | 3643 Hz  | 1.3  | -5.1 dB  |
| Peaking | 18324 Hz | 0.39 | -5.4 dB  |
| Peaking | 6886 Hz  | 7.09 | 2.5 dB   |
| Peaking | 8426 Hz  | 6.77 | -1.6 dB  |
| Peaking | 10822 Hz | 1.96 | 5.9 dB   |
| Peaking | 12310 Hz | 0.78 | -4.2 dB  |
| Peaking | 17053 Hz | 1.31 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -7.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Google%20Pixel%20Buds/Google%20Pixel%20Buds.png)