# Alpha Design Labs H128
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.8; 25 -7.3; 28 -7.9; 31 -8.4; 34 -8.8; 37 -9.1; 41 -9.5; 45 -9.7; 49 -9.9; 54 -10.1; 60 -10.3; 66 -10.5; 72 -10.7; 79 -11.0; 87 -11.2; 96 -11.4; 106 -11.2; 116 -11.0; 128 -10.9; 141 -11.5; 155 -11.7; 170 -11.1; 187 -10.9; 206 -10.7; 227 -10.5; 249 -10.2; 274 -9.7; 302 -9.5; 332 -9.1; 365 -8.8; 402 -8.5; 442 -8.5; 486 -8.5; 535 -8.5; 588 -8.2; 647 -8.1; 712 -8.2; 783 -7.9; 861 -7.5; 947 -6.5; 1042 -6.8; 1146 -7.2; 1261 -6.8; 1387 -6.7; 1526 -6.6; 1678 -6.5; 1846 -6.1; 2031 -5.6; 2234 -5.9; 2457 -5.0; 2703 -4.1; 2973 -3.2; 3270 -2.5; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 17 Hz   | 1.55 | 2.0 dB  |
| Peaking | 65 Hz   | 0.46 | -3.5 dB |
| Peaking | 177 Hz  | 0.75 | -2.8 dB |
| Peaking | 599 Hz  | 0.65 | -1.1 dB |
| Peaking | 4529 Hz | 1.26 | 6.9 dB  |
| Peaking | 1667 Hz | 3.68 | -0.3 dB |
| Peaking | 3694 Hz | 2.88 | 1.2 dB  |
| Peaking | 4507 Hz | 3.36 | -1.4 dB |
| Peaking | 6415 Hz | 3.12 | 4.1 dB  |
| Peaking | 7388 Hz | 1.5  | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20Design%20Labs%20H128/Alpha%20Design%20Labs%20H128.png)