# Klipsch X-10i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.2; 25 -8.3; 28 -8.4; 31 -8.5; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.8; 49 -9.0; 54 -9.2; 60 -9.5; 66 -9.8; 72 -10.0; 79 -10.1; 87 -10.4; 96 -10.8; 106 -10.8; 116 -11.0; 128 -11.1; 141 -11.4; 155 -11.4; 170 -11.4; 187 -11.4; 206 -11.2; 227 -11.1; 249 -10.9; 274 -10.6; 302 -10.3; 332 -9.9; 365 -9.4; 402 -9.0; 442 -8.7; 486 -8.3; 535 -7.8; 588 -7.3; 647 -6.8; 712 -6.5; 783 -6.3; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -7.9; 1526 -8.4; 1678 -8.4; 1846 -8.1; 2031 -7.9; 2234 -7.7; 2457 -7.7; 2703 -7.9; 2973 -7.3; 3270 -4.2; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X-10i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X-10i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.35 | -1.9 dB |
| Peaking | 149 Hz  | 0.76 | -3.4 dB |
| Peaking | 291 Hz  | 1.33 | -2.0 dB |
| Peaking | 2567 Hz | 1.12 | -4.4 dB |
| Peaking | 4317 Hz | 1.22 | 8.6 dB  |
| Peaking | 824 Hz  | 2.94 | 1.0 dB  |
| Peaking | 1528 Hz | 4.9  | -1.1 dB |
| Peaking | 4709 Hz | 4.74 | -2.2 dB |
| Peaking | 6422 Hz | 1.64 | 5.0 dB  |
| Peaking | 7473 Hz | 1.63 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20X-10i/Klipsch%20X-10i.png)