# Fidue A83
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.0; 25 -8.3; 28 -8.6; 31 -8.9; 34 -9.1; 37 -9.3; 41 -9.5; 45 -9.7; 49 -9.9; 54 -10.1; 60 -10.5; 66 -10.8; 72 -11.0; 79 -11.2; 87 -11.6; 96 -11.9; 106 -12.0; 116 -12.0; 128 -12.1; 141 -12.2; 155 -12.1; 170 -12.0; 187 -11.8; 206 -11.5; 227 -11.1; 249 -10.8; 274 -10.3; 302 -9.9; 332 -9.3; 365 -8.9; 402 -8.4; 442 -7.7; 486 -7.4; 535 -6.1; 588 -5.7; 647 -5.4; 712 -5.4; 783 -5.1; 861 -5.5; 947 -6.0; 1042 -6.8; 1146 -7.7; 1261 -9.0; 1387 -10.8; 1526 -12.7; 1678 -13.7; 1846 -13.3; 2031 -11.9; 2234 -10.8; 2457 -10.3; 2703 -10.9; 2973 -8.8; 3270 -4.5; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -3.1; 7010 -9.1; 7711 -14.7; 8482 -16.9; 9330 -15.1; 10263 -10.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A83 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A83 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 136 Hz   | 0.36 | -6.0 dB  |
| Peaking | 1686 Hz  | 1.28 | -15.8 dB |
| Peaking | 2752 Hz  | 1.73 | -13.9 dB |
| Peaking | 3338 Hz  | 0.37 | 17.6 dB  |
| Peaking | 8449 Hz  | 1.78 | -19.9 dB |
| Peaking | 626 Hz   | 3.88 | 0.8 dB   |
| Peaking | 4722 Hz  | 3.44 | -2.0 dB  |
| Peaking | 6279 Hz  | 1.89 | 3.0 dB   |
| Peaking | 7289 Hz  | 5.55 | -4.0 dB  |
| Peaking | 15917 Hz | 1.51 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.2 dB |
| Peaking | 4000 Hz  | 1.41 | 10.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.0 dB  |
| Peaking | 16000 Hz | 1.41 | 0.8 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A83/Fidue%20A83.png)