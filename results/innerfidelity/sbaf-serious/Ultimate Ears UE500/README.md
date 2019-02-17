# Ultimate Ears UE500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.2; 23 -15.1; 25 -15.1; 28 -15.0; 31 -14.8; 34 -14.7; 37 -14.6; 41 -14.4; 45 -14.2; 49 -14.1; 54 -14.0; 60 -13.9; 66 -13.8; 72 -13.7; 79 -13.7; 87 -13.7; 96 -13.6; 106 -13.4; 116 -13.2; 128 -13.1; 141 -12.9; 155 -12.6; 170 -12.3; 187 -11.9; 206 -11.6; 227 -11.1; 249 -10.7; 274 -10.3; 302 -9.8; 332 -9.3; 365 -8.8; 402 -8.3; 442 -7.8; 486 -7.4; 535 -7.0; 588 -6.4; 647 -6.1; 712 -6.0; 783 -5.7; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -7.3; 1261 -7.7; 1387 -7.8; 1526 -7.9; 1678 -8.7; 1846 -9.2; 2031 -9.7; 2234 -10.0; 2457 -9.4; 2703 -7.5; 2973 -4.1; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -5.6; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.44 | -7.6 dB |
| Peaking | 120 Hz  | 0.4  | -5.7 dB |
| Peaking | 693 Hz  | 1.42 | 1.8 dB  |
| Peaking | 2273 Hz | 1.43 | -6.9 dB |
| Peaking | 3908 Hz | 1.09 | 8.8 dB  |
| Peaking | 1254 Hz | 6.97 | -0.6 dB |
| Peaking | 3264 Hz | 8.1  | 1.8 dB  |
| Peaking | 4099 Hz | 3.39 | -1.3 dB |
| Peaking | 6251 Hz | 2.77 | 6.0 dB  |
| Peaking | 7017 Hz | 1.9  | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE500/Ultimate%20Ears%20UE500.png)