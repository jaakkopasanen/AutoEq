# Klipsch Reference ONE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.4; 25 -10.6; 28 -10.9; 31 -11.1; 34 -11.2; 37 -11.4; 41 -11.5; 45 -11.7; 49 -11.9; 54 -12.1; 60 -12.3; 66 -12.5; 72 -12.8; 79 -13.0; 87 -13.2; 96 -13.3; 106 -13.2; 116 -13.3; 128 -13.7; 141 -13.8; 155 -13.9; 170 -13.4; 187 -13.2; 206 -12.9; 227 -12.8; 249 -12.1; 274 -11.2; 302 -10.4; 332 -10.0; 365 -9.3; 402 -8.1; 442 -6.8; 486 -6.2; 535 -5.2; 588 -4.0; 647 -3.4; 712 -3.5; 783 -3.8; 861 -4.8; 947 -5.7; 1042 -6.5; 1146 -6.7; 1261 -6.7; 1387 -8.1; 1526 -8.6; 1678 -9.2; 1846 -9.2; 2031 -9.2; 2234 -9.5; 2457 -9.5; 2703 -9.6; 2973 -9.1; 3270 -8.0; 3597 -6.0; 3957 -3.5; 4353 -1.6; 4788 -0.5; 5267 -2.9; 5793 -3.8; 6373 -4.5; 7010 -4.0; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Reference ONE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.44 | -5.5 dB |
| Peaking | 140 Hz  | 1.15 | -4.7 dB |
| Peaking | 242 Hz  | 2.05 | -3.6 dB |
| Peaking | 4731 Hz | 4.36 | 6.3 dB  |
| Peaking | 17 Hz   | 1.85 | -0.9 dB |
| Peaking | 357 Hz  | 3.65 | -1.7 dB |
| Peaking | 687 Hz  | 1.64 | 4.0 dB  |
| Peaking | 2845 Hz | 0.78 | -8.1 dB |
| Peaking | 3816 Hz | 0.85 | 6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Reference%20ONE/Klipsch%20Reference%20ONE.png)