# Audio-Technica ATH-M60x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.6; 25 -5.7; 28 -5.9; 31 -6.0; 34 -6.2; 37 -6.3; 41 -6.5; 45 -6.6; 49 -6.8; 54 -7.0; 60 -7.1; 66 -7.3; 72 -7.4; 79 -7.5; 87 -7.7; 96 -8.0; 106 -8.2; 116 -8.4; 128 -8.6; 141 -8.7; 155 -8.8; 170 -8.9; 187 -8.7; 206 -8.5; 227 -8.2; 249 -7.8; 274 -7.3; 302 -6.4; 332 -5.0; 365 -2.7; 402 -0.6; 442 -0.5; 486 -2.3; 535 -4.8; 588 -6.3; 647 -7.2; 712 -7.5; 783 -7.6; 861 -7.4; 947 -7.4; 1042 -7.5; 1146 -7.5; 1261 -7.6; 1387 -7.6; 1526 -7.5; 1678 -7.8; 1846 -8.1; 2031 -7.8; 2234 -6.8; 2457 -5.4; 2703 -4.7; 2973 -4.0; 3270 -3.8; 3597 -4.5; 3957 -7.9; 4353 -9.5; 4788 -7.7; 5267 -5.4; 5793 -4.3; 6373 -6.0; 7010 -10.0; 7711 -9.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.4; 15026 -13.4; 16529 -13.2; 18182 -11.6; 20000 -13.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M60x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M60x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 372 Hz   | 0.29 | -3.4 dB |
| Peaking | 423 Hz   | 1.97 | 9.8 dB  |
| Peaking | 3576 Hz  | 1.62 | 4.5 dB  |
| Peaking | 4197 Hz  | 4.81 | -6.4 dB |
| Peaking | 17891 Hz | 0.64 | -6.9 dB |
| Peaking | 21 Hz    | 1    | 1.1 dB  |
| Peaking | 5921 Hz  | 6.37 | 2.7 dB  |
| Peaking | 7208 Hz  | 5.18 | -4.8 dB |
| Peaking | 13822 Hz | 0.86 | 3.8 dB  |
| Peaking | 14867 Hz | 2.26 | -6.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -7.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M60x/Audio-Technica%20ATH-M60x.png)