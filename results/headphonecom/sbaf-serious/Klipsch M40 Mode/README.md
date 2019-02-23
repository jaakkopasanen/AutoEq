# Klipsch M40 Mode
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -11.0; 25 -11.2; 28 -11.4; 31 -11.5; 34 -11.5; 37 -11.5; 41 -11.4; 45 -11.3; 49 -11.2; 54 -11.2; 60 -11.1; 66 -11.1; 72 -11.1; 79 -11.1; 87 -11.1; 96 -11.1; 106 -11.1; 116 -11.0; 128 -11.3; 141 -11.3; 155 -11.2; 170 -11.2; 187 -11.2; 206 -11.1; 227 -11.1; 249 -11.0; 274 -10.8; 302 -10.3; 332 -9.6; 365 -9.7; 402 -9.8; 442 -9.8; 486 -9.9; 535 -9.6; 588 -9.4; 647 -9.2; 712 -9.3; 783 -9.4; 861 -9.8; 947 -10.2; 1042 -10.7; 1146 -11.5; 1261 -12.6; 1387 -14.1; 1526 -15.7; 1678 -15.7; 1846 -13.3; 2031 -9.7; 2234 -7.0; 2457 -4.4; 2703 -2.0; 2973 -1.2; 3270 -0.7; 3597 -1.6; 3957 -3.4; 4353 -3.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch M40 Mode GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch M40 Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 28 Hz   |  0.63 | -3.9 dB  |
| Peaking | 166 Hz  |  0.32 | -4.3 dB  |
| Peaking | 1621 Hz |  1.55 | -10.7 dB |
| Peaking | 2874 Hz |  1.57 | 7.8 dB   |
| Peaking | 5570 Hz |  2.6  | 6.0 dB   |
| Peaking | 242 Hz  |  6.08 | -0.3 dB  |
| Peaking | 4118 Hz | 18.11 | -1.7 dB  |
| Peaking | 6534 Hz |  7.61 | 2.1 dB   |
| Peaking | 7876 Hz |  2.59 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -4.4 dB |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20M40%20Mode/Klipsch%20M40%20Mode.png)