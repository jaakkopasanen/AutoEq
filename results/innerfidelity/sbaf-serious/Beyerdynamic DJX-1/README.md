# Beyerdynamic DJX-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.7; 34 -2.3; 37 -2.7; 41 -3.2; 45 -3.6; 49 -4.0; 54 -4.4; 60 -4.7; 66 -4.9; 72 -5.0; 79 -5.5; 87 -5.4; 96 -5.7; 106 -6.1; 116 -6.5; 128 -6.9; 141 -7.5; 155 -7.8; 170 -7.7; 187 -8.2; 206 -8.5; 227 -8.6; 249 -8.7; 274 -8.6; 302 -8.4; 332 -8.0; 365 -7.6; 402 -7.3; 442 -7.3; 486 -7.7; 535 -8.4; 588 -8.5; 647 -8.8; 712 -9.0; 783 -8.7; 861 -8.5; 947 -7.8; 1042 -7.8; 1146 -8.1; 1261 -7.8; 1387 -7.8; 1526 -7.6; 1678 -7.7; 1846 -7.3; 2031 -6.7; 2234 -6.4; 2457 -6.1; 2703 -5.4; 2973 -4.9; 3270 -4.6; 3597 -3.9; 3957 -1.5; 4353 -0.6; 4788 -0.6; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -10.7; 9330 -10.5; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DJX-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DJX-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.5  | 6.3 dB  |
| Peaking | 214 Hz   | 1.34 | -1.9 dB |
| Peaking | 1088 Hz  | 0.4  | -2.0 dB |
| Peaking | 5483 Hz  | 0.92 | 7.6 dB  |
| Peaking | 8731 Hz  | 2.49 | -8.2 dB |
| Peaking | 422 Hz   | 4.97 | 0.9 dB  |
| Peaking | 666 Hz   | 3.2  | -0.9 dB |
| Peaking | 1953 Hz  | 0.3  | 0.2 dB  |
| Peaking | 3378 Hz  | 8.36 | -1.0 dB |
| Peaking | 14852 Hz | 1.78 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DJX-1/Beyerdynamic%20DJX-1.png)