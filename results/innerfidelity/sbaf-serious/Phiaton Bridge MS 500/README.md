# Phiaton Bridge MS 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.4; 25 -7.8; 28 -8.3; 31 -8.7; 34 -9.0; 37 -9.2; 41 -9.5; 45 -9.7; 49 -10.0; 54 -10.2; 60 -10.2; 66 -10.3; 72 -10.5; 79 -10.7; 87 -10.5; 96 -10.4; 106 -10.0; 116 -10.2; 128 -10.4; 141 -10.1; 155 -9.3; 170 -8.3; 187 -7.8; 206 -6.9; 227 -5.8; 249 -4.9; 274 -4.2; 302 -4.2; 332 -4.5; 365 -4.8; 402 -5.3; 442 -5.9; 486 -6.7; 535 -7.4; 588 -7.8; 647 -8.4; 712 -8.9; 783 -9.4; 861 -9.7; 947 -9.6; 1042 -10.5; 1146 -10.6; 1261 -10.5; 1387 -10.2; 1526 -9.6; 1678 -10.0; 1846 -10.5; 2031 -8.7; 2234 -6.7; 2457 -4.6; 2703 -4.0; 2973 -4.7; 3270 -6.4; 3597 -7.8; 3957 -8.4; 4353 -6.6; 4788 -3.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Bridge MS 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge MS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 61 Hz   | 0.96 | -4.2 dB |
| Peaking | 128 Hz  | 2.88 | -2.9 dB |
| Peaking | 1201 Hz | 1.31 | -4.5 dB |
| Peaking | 5800 Hz | 2.85 | 7.2 dB  |
| Peaking | 8142 Hz | 2.4  | -1.1 dB |
| Peaking | 308 Hz  | 2.1  | 3.1 dB  |
| Peaking | 734 Hz  | 2.11 | -1.5 dB |
| Peaking | 1909 Hz | 2.67 | -5.5 dB |
| Peaking | 2554 Hz | 1    | 5.2 dB  |
| Peaking | 3776 Hz | 2.72 | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Bridge%20MS%20500/Phiaton%20Bridge%20MS%20500.png)