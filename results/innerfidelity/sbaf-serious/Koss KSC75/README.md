# Koss KSC75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.6; 60 -2.8; 66 -3.9; 72 -4.8; 79 -5.7; 87 -6.5; 96 -7.2; 106 -7.7; 116 -7.9; 128 -8.2; 141 -8.2; 155 -8.2; 170 -8.0; 187 -7.7; 206 -7.6; 227 -7.4; 249 -7.2; 274 -6.9; 302 -6.5; 332 -6.2; 365 -6.0; 402 -5.6; 442 -5.3; 486 -5.2; 535 -5.0; 588 -4.6; 647 -4.6; 712 -4.5; 783 -4.3; 861 -4.5; 947 -4.6; 1042 -4.7; 1146 -4.9; 1261 -5.3; 1387 -6.1; 1526 -7.2; 1678 -8.1; 1846 -9.1; 2031 -9.6; 2234 -10.5; 2457 -10.3; 2703 -8.9; 2973 -7.6; 3270 -7.7; 3597 -0.9; 3957 -0.5; 4353 -9.0; 4788 -14.1; 5267 -7.6; 5793 -3.3; 6373 -3.0; 7010 -4.0; 7711 -6.2; 8482 -8.7; 9330 -11.4; 10263 -9.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 1.12 | 7.3 dB   |
| Peaking | 2413 Hz | 1.08 | -15.7 dB |
| Peaking | 3576 Hz | 0.41 | 13.5 dB  |
| Peaking | 4769 Hz | 5.66 | -15.4 dB |
| Peaking | 9308 Hz | 1.84 | -9.5 dB  |
| Peaking | 57 Hz   | 2    | 3.1 dB   |
| Peaking | 144 Hz  | 0.53 | -2.9 dB  |
| Peaking | 1631 Hz | 2.87 | -1.5 dB  |
| Peaking | 2362 Hz | 0.08 | 2.0 dB   |
| Peaking | 6536 Hz | 0.14 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20KSC75/Koss%20KSC75.png)