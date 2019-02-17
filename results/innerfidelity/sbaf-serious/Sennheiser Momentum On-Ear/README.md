# Sennheiser Momentum On-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.2; 25 -10.3; 28 -10.4; 31 -10.6; 34 -10.7; 37 -10.8; 41 -10.9; 45 -10.9; 49 -11.0; 54 -11.0; 60 -11.0; 66 -11.0; 72 -10.9; 79 -10.9; 87 -11.0; 96 -11.1; 106 -11.1; 116 -11.0; 128 -11.1; 141 -10.9; 155 -10.7; 170 -10.2; 187 -9.8; 206 -9.3; 227 -8.5; 249 -7.6; 274 -6.7; 302 -5.8; 332 -5.3; 365 -5.0; 402 -4.8; 442 -4.6; 486 -4.9; 535 -5.2; 588 -5.5; 647 -6.1; 712 -6.7; 783 -6.6; 861 -6.4; 947 -6.3; 1042 -6.7; 1146 -7.5; 1261 -8.6; 1387 -9.8; 1526 -10.9; 1678 -11.7; 1846 -11.9; 2031 -10.9; 2234 -9.8; 2457 -7.8; 2703 -6.0; 2973 -4.4; 3270 -3.1; 3597 -1.7; 3957 -0.5; 4353 -0.5; 4788 -5.3; 5267 -5.0; 5793 -3.7; 6373 -5.2; 7010 -7.2; 7711 -7.5; 8482 -8.5; 9330 -8.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.53 | -4.6 dB |
| Peaking | 135 Hz   | 1.55 | -3.4 dB |
| Peaking | 1811 Hz  | 2.12 | -6.4 dB |
| Peaking | 3886 Hz  | 2.08 | 6.6 dB  |
| Peaking | 8780 Hz  | 3.86 | -2.9 dB |
| Peaking | 18 Hz    | 1.85 | -0.9 dB |
| Peaking | 206 Hz   | 2.89 | -1.3 dB |
| Peaking | 326 Hz   | 2.47 | 1.2 dB  |
| Peaking | 456 Hz   | 1.78 | 2.0 dB  |
| Peaking | 10747 Hz | 3.37 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)