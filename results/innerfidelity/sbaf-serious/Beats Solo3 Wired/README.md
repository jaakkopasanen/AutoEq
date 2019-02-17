# Beats Solo3 Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.2; 25 -9.3; 28 -9.4; 31 -9.4; 34 -9.5; 37 -9.6; 41 -9.5; 45 -9.6; 49 -9.7; 54 -9.7; 60 -9.8; 66 -10.0; 72 -10.0; 79 -10.3; 87 -10.4; 96 -10.7; 106 -11.1; 116 -11.0; 128 -11.0; 141 -11.2; 155 -11.3; 170 -11.0; 187 -11.2; 206 -10.9; 227 -10.4; 249 -10.0; 274 -9.2; 302 -8.5; 332 -7.7; 365 -7.0; 402 -5.9; 442 -5.3; 486 -5.2; 535 -4.7; 588 -3.7; 647 -3.2; 712 -2.8; 783 -2.5; 861 -2.8; 947 -3.0; 1042 -3.2; 1146 -3.5; 1261 -3.8; 1387 -4.3; 1526 -4.6; 1678 -4.9; 1846 -4.7; 2031 -4.2; 2234 -4.1; 2457 -3.9; 2703 -4.4; 2973 -4.9; 3270 -5.6; 3597 -5.7; 3957 -3.5; 4353 -5.0; 4788 -5.2; 5267 -2.4; 5793 -0.5; 6373 -1.6; 7010 -1.5; 7711 -2.9; 8482 -3.2; 9330 -3.2; 10263 -3.2; 11289 -3.2; 12418 -3.2; 13660 -3.2; 15026 -3.2; 16529 -3.2; 18182 -3.8; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.29 | -5.9 dB |
| Peaking | 137 Hz  |  0.85 | -4.6 dB |
| Peaking | 247 Hz  |  1.35 | -3.9 dB |
| Peaking | 4022 Hz |  0.84 | -2.5 dB |
| Peaking | 6016 Hz |  2.68 | 4.1 dB  |
| Peaking | 785 Hz  |  2.61 | 1.5 dB  |
| Peaking | 1628 Hz |  3.18 | -1.2 dB |
| Peaking | 2462 Hz |  5.94 | 0.7 dB  |
| Peaking | 4063 Hz | 11.47 | 2.1 dB  |
| Peaking | 4638 Hz |  9.15 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -6.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo3%20Wired/Beats%20Solo3%20Wired.png)