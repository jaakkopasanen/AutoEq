# Shure SRH940
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.7; 41 -2.5; 45 -3.1; 49 -3.6; 54 -4.1; 60 -4.4; 66 -4.5; 72 -3.8; 79 -2.7; 87 -2.5; 96 -4.2; 106 -5.0; 116 -4.8; 128 -4.5; 141 -5.3; 155 -5.6; 170 -5.5; 187 -6.9; 206 -7.5; 227 -8.0; 249 -8.2; 274 -8.2; 302 -8.0; 332 -9.2; 365 -8.1; 402 -7.6; 442 -7.3; 486 -6.9; 535 -6.6; 588 -6.2; 647 -5.9; 712 -5.8; 783 -5.3; 861 -5.0; 947 -5.4; 1042 -5.3; 1146 -5.3; 1261 -5.7; 1387 -6.3; 1526 -7.0; 1678 -7.4; 1846 -7.3; 2031 -7.2; 2234 -7.0; 2457 -5.5; 2703 -5.7; 2973 -5.7; 3270 -6.2; 3597 -6.8; 3957 -7.8; 4353 -8.1; 4788 -7.4; 5267 -4.5; 5793 -2.2; 6373 -1.8; 7010 -4.0; 7711 -6.4; 8482 -12.6; 9330 -15.1; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -8.5; 16529 -7.0; 18182 -8.9; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH940 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.9  | 6.3 dB   |
| Peaking | 87 Hz    | 1.78 | 2.7 dB   |
| Peaking | 299 Hz   | 1.95 | -2.4 dB  |
| Peaking | 6358 Hz  | 3.79 | 5.9 dB   |
| Peaking | 9048 Hz  | 4.96 | -10.2 dB |
| Peaking | 953 Hz   | 1.61 | 1.4 dB   |
| Peaking | 1861 Hz  | 1.95 | -2.3 dB  |
| Peaking | 3358 Hz  | 0.66 | 2.0 dB   |
| Peaking | 4205 Hz  | 2.7  | -3.8 dB  |
| Peaking | 20013 Hz | 0.89 | -5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH940/Shure%20SRH940.png)