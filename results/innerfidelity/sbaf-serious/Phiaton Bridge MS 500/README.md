# Phiaton Bridge MS 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.7; 25 -4.1; 28 -4.6; 31 -4.9; 34 -5.3; 37 -5.5; 41 -5.8; 45 -6.0; 49 -6.2; 54 -6.4; 60 -6.5; 66 -6.6; 72 -6.8; 79 -7.0; 87 -6.8; 96 -6.6; 106 -6.3; 116 -6.5; 128 -6.7; 141 -6.3; 155 -5.6; 170 -4.6; 187 -4.1; 206 -3.2; 227 -2.1; 249 -1.2; 274 -0.6; 302 -0.6; 332 -0.8; 365 -1.1; 402 -1.6; 442 -2.1; 486 -3.0; 535 -3.7; 588 -4.0; 647 -4.7; 712 -5.1; 783 -5.7; 861 -6.0; 947 -5.9; 1042 -6.8; 1146 -6.9; 1261 -6.8; 1387 -6.5; 1526 -5.9; 1678 -6.3; 1846 -6.8; 2031 -5.0; 2234 -3.0; 2457 -0.8; 2703 -0.5; 2973 -1.0; 3270 -2.7; 3597 -4.0; 3957 -4.7; 4353 -2.9; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Bridge MS 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge MS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.88 | 3.3 dB  |
| Peaking | 318 Hz   | 1.21 | 6.4 dB  |
| Peaking | 2685 Hz  | 3.34 | 6.1 dB  |
| Peaking | 5683 Hz  | 1.81 | 7.0 dB  |
| Peaking | 7965 Hz  | 2.07 | -2.2 dB |
| Peaking | 99 Hz    | 1.23 | -0.8 dB |
| Peaking | 536 Hz   | 2.43 | 0.6 dB  |
| Peaking | 1140 Hz  | 3.44 | -1.2 dB |
| Peaking | 1815 Hz  | 9.08 | -1.5 dB |
| Peaking | 22050 Hz | 1.9  | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 5.5 dB  |
| Peaking | 500 Hz   | 1.41 | 3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Bridge%20MS%20500/Phiaton%20Bridge%20MS%20500.png)