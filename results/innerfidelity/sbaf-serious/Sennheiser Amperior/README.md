# Sennheiser Amperior
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.7; 25 -3.3; 28 -4.0; 31 -4.6; 34 -5.2; 37 -5.6; 41 -6.1; 45 -6.5; 49 -6.9; 54 -7.3; 60 -7.8; 66 -7.9; 72 -8.1; 79 -8.9; 87 -9.6; 96 -9.9; 106 -10.5; 116 -10.7; 128 -11.1; 141 -11.2; 155 -11.1; 170 -10.6; 187 -10.4; 206 -9.8; 227 -8.8; 249 -7.8; 274 -6.9; 302 -6.2; 332 -5.4; 365 -4.7; 402 -4.2; 442 -4.0; 486 -4.3; 535 -4.5; 588 -4.4; 647 -4.7; 712 -5.0; 783 -5.1; 861 -5.5; 947 -5.9; 1042 -6.1; 1146 -6.4; 1261 -6.8; 1387 -7.5; 1526 -8.2; 1678 -8.9; 1846 -9.3; 2031 -9.2; 2234 -8.3; 2457 -6.5; 2703 -5.1; 2973 -3.9; 3270 -3.7; 3597 -3.8; 3957 -3.6; 4353 -3.0; 4788 -2.7; 5267 -1.4; 5793 -0.6; 6373 -0.5; 7010 -3.4; 7711 -6.9; 8482 -11.3; 9330 -10.5; 10263 -6.2; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Amperior GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.98 | 4.0 dB   |
| Peaking | 130 Hz   | 1.12 | -5.7 dB  |
| Peaking | 1889 Hz  | 2.58 | -4.4 dB  |
| Peaking | 6567 Hz  | 0.94 | 7.7 dB   |
| Peaking | 8668 Hz  | 2.5  | -11.4 dB |
| Peaking | 210 Hz   | 2.64 | -1.8 dB  |
| Peaking | 452 Hz   | 0.96 | 2.8 dB   |
| Peaking | 2606 Hz  | 0.09 | -0.5 dB  |
| Peaking | 3042 Hz  | 4.32 | 1.6 dB   |
| Peaking | 10209 Hz | 4.75 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)