# Klipsch X12i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.3; 25 -7.5; 28 -7.6; 31 -7.8; 34 -7.9; 37 -8.0; 41 -8.2; 45 -8.4; 49 -8.5; 54 -8.8; 60 -9.0; 66 -9.3; 72 -9.6; 79 -10.0; 87 -10.3; 96 -10.7; 106 -10.9; 116 -11.1; 128 -11.3; 141 -11.5; 155 -11.6; 170 -11.6; 187 -11.6; 206 -11.5; 227 -11.3; 249 -11.1; 274 -10.9; 302 -10.6; 332 -10.3; 365 -9.9; 402 -9.6; 442 -9.0; 486 -8.7; 535 -8.3; 588 -7.6; 647 -7.1; 712 -6.8; 783 -6.3; 861 -6.2; 947 -6.3; 1042 -6.4; 1146 -6.5; 1261 -6.6; 1387 -6.9; 1526 -7.2; 1678 -7.1; 1846 -6.7; 2031 -6.1; 2234 -5.8; 2457 -5.4; 2703 -5.5; 2973 -5.6; 3270 -4.6; 3597 -2.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X12i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X12i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 127 Hz  | 0.54 | -4.4 dB |
| Peaking | 286 Hz  | 1.11 | -2.2 dB |
| Peaking | 1618 Hz | 5.38 | -0.9 dB |
| Peaking | 4210 Hz | 2.33 | 5.9 dB  |
| Peaking | 5889 Hz | 3.38 | 5.0 dB  |
| Peaking | 26 Hz   | 1.41 | -0.3 dB |
| Peaking | 481 Hz  | 2.3  | -1.0 dB |
| Peaking | 535 Hz  | 1.39 | 0.6 dB  |
| Peaking | 838 Hz  | 3.09 | 0.9 dB  |
| Peaking | 8230 Hz | 4.35 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X12i/Klipsch%20X12i.png)