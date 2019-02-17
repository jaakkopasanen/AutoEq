# NarMoo W1M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -12.0; 25 -12.0; 28 -12.0; 31 -12.0; 34 -11.9; 37 -11.9; 41 -11.8; 45 -11.7; 49 -11.7; 54 -11.6; 60 -11.6; 66 -11.5; 72 -11.5; 79 -11.6; 87 -11.6; 96 -11.7; 106 -11.5; 116 -11.4; 128 -11.3; 141 -11.2; 155 -11.1; 170 -10.9; 187 -10.7; 206 -10.5; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.4; 332 -9.2; 365 -8.9; 402 -8.7; 442 -8.4; 486 -8.3; 535 -8.0; 588 -7.5; 647 -7.3; 712 -7.2; 783 -6.8; 861 -6.7; 947 -6.6; 1042 -6.2; 1146 -5.9; 1261 -5.5; 1387 -5.2; 1526 -4.9; 1678 -4.6; 1846 -4.1; 2031 -3.7; 2234 -3.6; 2457 -3.5; 2703 -2.9; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -3.1; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo W1M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo W1M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  0.41 | -4.7 dB |
| Peaking | 132 Hz  |  0.37 | -4.2 dB |
| Peaking | 3630 Hz |  0.89 | 6.2 dB  |
| Peaking | 6170 Hz |  3.3  | 5.6 dB  |
| Peaking | 7104 Hz |  1.16 | -2.6 dB |
| Peaking | 2538 Hz |  3.33 | -2.2 dB |
| Peaking | 2565 Hz |  1.23 | 1.2 dB  |
| Peaking | 4885 Hz | 10.4  | -2.2 dB |
| Peaking | 5346 Hz |  7.53 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20W1M/NarMoo%20W1M.png)