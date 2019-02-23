# Apple iPod Ear Buds sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.6; 155 -2.0; 170 -3.5; 187 -4.7; 206 -6.0; 227 -6.9; 249 -7.6; 274 -8.0; 302 -8.2; 332 -8.1; 365 -8.0; 402 -7.6; 442 -6.7; 486 -6.5; 535 -6.2; 588 -6.1; 647 -6.4; 712 -6.6; 783 -6.5; 861 -6.6; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.5; 1387 -6.9; 1526 -7.3; 1678 -7.6; 1846 -7.3; 2031 -6.2; 2234 -5.1; 2457 -6.3; 2703 -9.4; 2973 -11.7; 3270 -10.3; 3597 -7.2; 3957 -6.1; 4353 -7.0; 4788 -6.9; 5267 -5.8; 5793 -9.2; 6373 -13.2; 7010 -10.7; 7711 -9.3; 8482 -10.8; 9330 -9.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple iPod Ear Buds sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple iPod Ear Buds sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 62 Hz   |  0.2  | 6.6 dB  |
| Peaking | 221 Hz  |  2.81 | -2.6 dB |
| Peaking | 317 Hz  |  1.33 | -4.7 dB |
| Peaking | 3011 Hz |  6.25 | -5.7 dB |
| Peaking | 6732 Hz |  3    | -5.9 dB |
| Peaking | 11 Hz   |  2.62 | 0.5 dB  |
| Peaking | 136 Hz  |  6.4  | 1.2 dB  |
| Peaking | 3920 Hz |  7.67 | 1.2 dB  |
| Peaking | 5316 Hz | 10.68 | 2.8 dB  |
| Peaking | 8703 Hz |  8.23 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20iPod%20Ear%20Buds%20sample%20A/Apple%20iPod%20Ear%20Buds%20sample%20A.png)