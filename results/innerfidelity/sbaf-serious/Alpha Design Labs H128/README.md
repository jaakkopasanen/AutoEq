# Alpha Design Labs H128
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -7.1; 25 -7.7; 28 -8.3; 31 -8.8; 34 -9.2; 37 -9.5; 41 -9.9; 45 -10.1; 49 -10.3; 54 -10.5; 60 -10.7; 66 -10.9; 72 -11.1; 79 -11.3; 87 -11.6; 96 -11.7; 106 -11.6; 116 -11.4; 128 -11.3; 141 -11.8; 155 -12.1; 170 -11.5; 187 -11.3; 206 -11.0; 227 -10.9; 249 -10.6; 274 -10.1; 302 -9.8; 332 -9.5; 365 -9.2; 402 -8.9; 442 -8.9; 486 -8.9; 535 -8.9; 588 -8.5; 647 -8.5; 712 -8.5; 783 -8.2; 861 -7.9; 947 -6.9; 1042 -7.2; 1146 -7.6; 1261 -7.2; 1387 -7.1; 1526 -7.0; 1678 -6.9; 1846 -6.5; 2031 -6.0; 2234 -6.2; 2457 -5.4; 2703 -4.4; 2973 -3.5; 3270 -2.9; 3597 -1.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Alpha Design Labs H128 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alpha Design Labs H128 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.67 | -2.8 dB |
| Peaking | 165 Hz  | 0.55 | -4.4 dB |
| Peaking | 635 Hz  | 1.38 | -1.2 dB |
| Peaking | 1585 Hz | 1.59 | -0.8 dB |
| Peaking | 4577 Hz | 1.31 | 6.9 dB  |
| Peaking | 3747 Hz | 4.2  | 1.2 dB  |
| Peaking | 4507 Hz | 3.58 | -1.2 dB |
| Peaking | 6284 Hz | 3.31 | 3.7 dB  |
| Peaking | 7883 Hz | 1.49 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20Design%20Labs%20H128/Alpha%20Design%20Labs%20H128.png)