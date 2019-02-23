# Phiaton PS 320
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.5; 25 -4.7; 28 -4.8; 31 -5.0; 34 -5.1; 37 -5.1; 41 -5.2; 45 -5.4; 49 -5.7; 54 -5.9; 60 -6.1; 66 -6.3; 72 -6.0; 79 -6.0; 87 -6.9; 96 -7.9; 106 -8.9; 116 -9.0; 128 -9.5; 141 -9.9; 155 -10.3; 170 -10.1; 187 -10.1; 206 -9.8; 227 -8.8; 249 -9.0; 274 -9.9; 302 -9.8; 332 -9.2; 365 -7.9; 402 -6.6; 442 -5.1; 486 -3.8; 535 -3.3; 588 -2.5; 647 -2.5; 712 -3.6; 783 -4.5; 861 -5.5; 947 -6.3; 1042 -6.9; 1146 -7.3; 1261 -7.6; 1387 -8.9; 1526 -9.4; 1678 -9.8; 1846 -9.9; 2031 -9.9; 2234 -10.5; 2457 -8.9; 2703 -7.1; 2973 -5.2; 3270 -3.9; 3597 -1.6; 3957 -1.2; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -5.6; 7010 -5.3; 7711 -6.2; 8482 -7.6; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.9; 18182 -10.2; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 320 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 223 Hz   |  0.71 | -4.1 dB |
| Peaking | 588 Hz   |  1.6  | 5.7 dB  |
| Peaking | 1986 Hz  |  1.21 | -5.0 dB |
| Peaking | 4322 Hz  |  1.53 | 7.7 dB  |
| Peaking | 18727 Hz |  0.85 | -4.0 dB |
| Peaking | 26 Hz    |  0.94 | 2.1 dB  |
| Peaking | 77 Hz    |  6.04 | 1.3 dB  |
| Peaking | 1413 Hz  |  2.81 | -0.1 dB |
| Peaking | 5622 Hz  | 11.22 | 2.8 dB  |
| Peaking | 8944 Hz  |  4.67 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20320/Phiaton%20PS%20320.png)