# Sennheiser Momentum Wireless Wired Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.9; 25 -8.3; 28 -8.3; 31 -8.0; 34 -7.6; 37 -7.4; 41 -7.1; 45 -6.8; 49 -6.6; 54 -6.4; 60 -6.2; 66 -6.0; 72 -6.0; 79 -6.0; 87 -6.0; 96 -6.0; 106 -5.9; 116 -5.7; 128 -5.6; 141 -5.6; 155 -5.4; 170 -5.3; 187 -4.9; 206 -4.7; 227 -4.3; 249 -4.2; 274 -4.0; 302 -3.8; 332 -3.6; 365 -3.4; 402 -3.6; 442 -4.0; 486 -4.8; 535 -5.7; 588 -6.3; 647 -7.2; 712 -8.1; 783 -8.6; 861 -9.5; 947 -10.2; 1042 -10.8; 1146 -11.3; 1261 -12.2; 1387 -13.3; 1526 -14.8; 1678 -15.5; 1846 -16.3; 2031 -16.3; 2234 -14.9; 2457 -12.1; 2703 -9.8; 2973 -6.9; 3270 -4.7; 3597 -2.9; 3957 -1.2; 4353 -0.5; 4788 -8.6; 5267 -7.0; 5793 -2.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum Wireless Wired Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 26 Hz   |  2.19 | -1.9 dB  |
| Peaking | 367 Hz  |  0.74 | 4.2 dB   |
| Peaking | 2060 Hz |  0.77 | -18.8 dB |
| Peaking | 3145 Hz |  0.67 | 12.3 dB  |
| Peaking | 4075 Hz |  6.19 | 4.1 dB   |
| Peaking | 4548 Hz | 10.93 | 5.0 dB   |
| Peaking | 4967 Hz |  6.42 | -9.2 dB  |
| Peaking | 6241 Hz |  2.96 | 5.9 dB   |
| Peaking | 7503 Hz |  3.35 | -2.0 dB  |
| Peaking | 9577 Hz |  1.28 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB   |
| Peaking | 125 Hz   | 1.41 | 0.2 dB   |
| Peaking | 250 Hz   | 1.41 | 2.6 dB   |
| Peaking | 500 Hz   | 1.41 | 2.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -11.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Wired%20Active/Sennheiser%20Momentum%20Wireless%20Wired%20Active.png)