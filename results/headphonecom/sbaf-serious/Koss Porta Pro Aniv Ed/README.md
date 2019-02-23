# Koss Porta Pro Aniv Ed
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.4; 37 -2.3; 41 -3.4; 45 -4.3; 49 -5.2; 54 -6.2; 60 -7.2; 66 -8.1; 72 -9.0; 79 -9.7; 87 -10.4; 96 -10.9; 106 -11.3; 116 -11.3; 128 -11.4; 141 -11.3; 155 -11.4; 170 -11.2; 187 -10.9; 206 -10.4; 227 -10.0; 249 -9.4; 274 -8.9; 302 -8.5; 332 -7.9; 365 -7.5; 402 -7.1; 442 -6.8; 486 -6.2; 535 -6.0; 588 -5.7; 647 -5.4; 712 -5.4; 783 -5.2; 861 -5.3; 947 -5.4; 1042 -5.6; 1146 -5.7; 1261 -6.1; 1387 -6.9; 1526 -7.9; 1678 -8.8; 1846 -9.6; 2031 -10.0; 2234 -9.7; 2457 -8.0; 2703 -5.6; 2973 -2.9; 3270 -1.2; 3597 -0.6; 3957 -3.9; 4353 -4.7; 4788 -5.5; 5267 -3.0; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro Aniv Ed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro Aniv Ed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.91 | 7.0 dB  |
| Peaking | 122 Hz  | 0.74 | -5.8 dB |
| Peaking | 2075 Hz | 2.94 | -4.6 dB |
| Peaking | 3367 Hz | 3.26 | 6.4 dB  |
| Peaking | 6016 Hz | 4.28 | 6.4 dB  |
| Peaking | 241 Hz  | 1.84 | -0.9 dB |
| Peaking | 785 Hz  | 0.93 | 1.7 dB  |
| Peaking | 1633 Hz | 4.15 | -1.4 dB |
| Peaking | 8876 Hz | 6.51 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Porta%20Pro%20Aniv%20Ed/Koss%20Porta%20Pro%20Aniv%20Ed.png)