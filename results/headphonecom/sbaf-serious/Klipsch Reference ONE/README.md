# Klipsch Reference ONE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -14.0; 25 -14.2; 28 -14.4; 31 -14.5; 34 -14.6; 37 -14.7; 41 -14.7; 45 -14.7; 49 -14.6; 54 -14.7; 60 -14.7; 66 -14.7; 72 -14.6; 79 -14.5; 87 -14.5; 96 -14.5; 106 -14.2; 116 -13.6; 128 -13.1; 141 -13.6; 155 -13.6; 170 -13.0; 187 -12.8; 206 -12.1; 227 -12.1; 249 -11.7; 274 -11.2; 302 -10.4; 332 -9.4; 365 -8.2; 402 -6.9; 442 -5.4; 486 -4.3; 535 -4.0; 588 -3.5; 647 -3.3; 712 -3.4; 783 -3.7; 861 -4.5; 947 -5.5; 1042 -6.5; 1146 -6.9; 1261 -7.5; 1387 -8.7; 1526 -10.2; 1678 -11.0; 1846 -11.3; 2031 -11.1; 2234 -11.1; 2457 -10.8; 2703 -10.6; 2973 -10.5; 3270 -9.7; 3597 -7.9; 3957 -5.7; 4353 -3.5; 4788 -0.5; 5267 -4.9; 5793 -6.9; 6373 -3.0; 7010 -3.6; 7711 -5.8; 8482 -6.1; 9330 -6.2; 10263 -6.4; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Reference ONE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.42 | -8.6 dB |
| Peaking | 123 Hz  | 1.03 | -4.5 dB |
| Peaking | 236 Hz  | 2.36 | -3.8 dB |
| Peaking | 2267 Hz | 1.4  | -5.9 dB |
| Peaking | 4727 Hz | 4.84 | 6.3 dB  |
| Peaking | 327 Hz  | 2.73 | -2.1 dB |
| Peaking | 622 Hz  | 1.25 | 3.9 dB  |
| Peaking | 1563 Hz | 3.44 | -2.2 dB |
| Peaking | 5703 Hz | 7.14 | -2.4 dB |
| Peaking | 6623 Hz | 6.84 | 4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Reference%20ONE/Klipsch%20Reference%20ONE.png)