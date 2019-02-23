# AKG K271 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.1; 41 -2.0; 45 -2.8; 49 -3.4; 54 -4.0; 60 -4.4; 66 -4.4; 72 -3.7; 79 -2.6; 87 -1.5; 96 -1.5; 106 -3.9; 116 -4.9; 128 -5.3; 141 -6.3; 155 -5.9; 170 -5.6; 187 -6.2; 206 -6.1; 227 -6.9; 249 -7.5; 274 -7.8; 302 -7.9; 332 -8.0; 365 -8.0; 402 -8.2; 442 -8.2; 486 -8.6; 535 -8.9; 588 -9.1; 647 -10.1; 712 -7.9; 783 -6.0; 861 -6.6; 947 -6.8; 1042 -7.5; 1146 -7.9; 1261 -8.3; 1387 -9.0; 1526 -10.0; 1678 -10.6; 1846 -9.8; 2031 -6.8; 2234 -6.8; 2457 -5.2; 2703 -5.2; 2973 -4.4; 3270 -3.6; 3597 -2.6; 3957 -2.7; 4353 -4.5; 4788 -3.2; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.4; 8482 -12.9; 9330 -15.0; 10263 -11.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K271 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.91 | 6.5 dB   |
| Peaking | 91 Hz   | 3.7  | 4.9 dB   |
| Peaking | 1586 Hz | 1.67 | -4.4 dB  |
| Peaking | 6678 Hz | 0.73 | 8.9 dB   |
| Peaking | 9034 Hz | 2.16 | -15.8 dB |
| Peaking | 667 Hz  | 1.11 | -5.9 dB  |
| Peaking | 798 Hz  | 1.52 | 5.2 dB   |
| Peaking | 3901 Hz | 2.31 | 2.2 dB   |
| Peaking | 4429 Hz | 3.99 | -4.4 dB  |
| Peaking | 5325 Hz | 4.11 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K271%20MKII/AKG%20K271%20MKII.png)