# Zoukbox ZLX30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.7; 23 -15.7; 25 -15.7; 28 -15.7; 31 -15.6; 34 -15.6; 37 -15.5; 41 -15.4; 45 -15.2; 49 -15.1; 54 -15.0; 60 -14.9; 66 -14.9; 72 -14.8; 79 -14.7; 87 -14.7; 96 -14.6; 106 -14.3; 116 -14.0; 128 -13.7; 141 -13.4; 155 -13.1; 170 -12.7; 187 -12.2; 206 -11.7; 227 -11.1; 249 -10.6; 274 -10.0; 302 -9.4; 332 -8.9; 365 -8.2; 402 -7.8; 442 -7.1; 486 -6.7; 535 -6.3; 588 -5.6; 647 -5.3; 712 -5.2; 783 -4.9; 861 -5.1; 947 -5.6; 1042 -6.2; 1146 -6.7; 1261 -7.3; 1387 -8.3; 1526 -9.5; 1678 -10.5; 1846 -11.5; 2031 -12.5; 2234 -13.4; 2457 -13.1; 2703 -11.2; 2973 -7.8; 3270 -7.0; 3597 -9.2; 3957 -13.3; 4353 -16.0; 4788 -11.6; 5267 -3.0; 5793 -0.6; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -8.5; 11289 -6.6; 12418 -5.9; 13660 -5.9; 15026 -6.8; 16529 -8.3; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zoukbox ZLX30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zoukbox ZLX30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.25 | -9.6 dB  |
| Peaking | 153 Hz   | 0.81 | -3.8 dB  |
| Peaking | 2164 Hz  | 2.18 | -7.7 dB  |
| Peaking | 4373 Hz  | 4.46 | -12.0 dB |
| Peaking | 5840 Hz  | 3.2  | 8.2 dB   |
| Peaking | 766 Hz   | 2    | 1.9 dB   |
| Peaking | 1554 Hz  | 3.97 | -1.4 dB  |
| Peaking | 3201 Hz  | 9.48 | 2.4 dB   |
| Peaking | 10462 Hz | 6.98 | -3.2 dB  |
| Peaking | 16176 Hz | 3.97 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -2.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zoukbox%20ZLX30/Zoukbox%20ZLX30.png)