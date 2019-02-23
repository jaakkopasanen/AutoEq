# Beyerdynamic Aventho Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.8; 25 -3.5; 28 -4.5; 31 -5.2; 34 -5.8; 37 -6.3; 41 -6.8; 45 -7.1; 49 -7.4; 54 -7.9; 60 -8.5; 66 -9.2; 72 -9.9; 79 -10.6; 87 -11.4; 96 -12.0; 106 -12.6; 116 -12.8; 128 -12.8; 141 -12.4; 155 -11.8; 170 -10.8; 187 -9.5; 206 -8.5; 227 -7.7; 249 -7.0; 274 -6.2; 302 -6.3; 332 -6.8; 365 -7.2; 402 -7.1; 442 -7.0; 486 -7.2; 535 -7.4; 588 -7.5; 647 -7.7; 712 -7.9; 783 -8.2; 861 -8.4; 947 -8.2; 1042 -8.2; 1146 -8.2; 1261 -7.9; 1387 -7.5; 1526 -6.9; 1678 -6.2; 1846 -5.2; 2031 -4.1; 2234 -2.7; 2457 -0.5; 2703 -1.6; 2973 -1.9; 3270 -1.3; 3597 -0.9; 3957 -0.7; 4353 -1.6; 4788 -4.1; 5267 -5.9; 5793 -5.4; 6373 -2.0; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Aventho Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Aventho Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.7  | 4.5 dB  |
| Peaking | 114 Hz   | 0.96 | -7.1 dB |
| Peaking | 2495 Hz  | 4.52 | 4.6 dB  |
| Peaking | 3773 Hz  | 2.29 | 5.4 dB  |
| Peaking | 21378 Hz | 2.3  | 0.3 dB  |
| Peaking | 156 Hz   | 5.49 | -0.8 dB |
| Peaking | 270 Hz   | 3.26 | 1.6 dB  |
| Peaking | 931 Hz   | 1.18 | -2.5 dB |
| Peaking | 5386 Hz  | 6.44 | -1.8 dB |
| Peaking | 6570 Hz  | 8.05 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20Aventho%20Wireless/Beyerdynamic%20Aventho%20Wireless.png)