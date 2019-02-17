# Soul Jet Pro ANC On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -9.1; 25 -10.6; 28 -12.4; 31 -13.5; 34 -13.7; 37 -13.4; 41 -12.8; 45 -12.3; 49 -12.0; 54 -11.8; 60 -11.6; 66 -11.5; 72 -11.5; 79 -11.5; 87 -11.6; 96 -11.9; 106 -12.0; 116 -12.1; 128 -12.7; 141 -13.3; 155 -13.6; 170 -13.7; 187 -14.1; 206 -14.4; 227 -14.4; 249 -14.7; 274 -14.7; 302 -14.9; 332 -15.1; 365 -15.1; 402 -14.9; 442 -13.8; 486 -10.3; 535 -5.1; 588 -2.2; 647 -0.5; 712 -1.2; 783 -1.4; 861 -2.9; 947 -4.5; 1042 -5.9; 1146 -7.2; 1261 -8.6; 1387 -10.4; 1526 -13.5; 1678 -16.0; 1846 -18.7; 2031 -20.9; 2234 -20.7; 2457 -18.0; 2703 -15.1; 2973 -11.6; 3270 -9.4; 3597 -10.3; 3957 -12.8; 4353 -16.3; 4788 -13.3; 5267 -9.2; 5793 -4.8; 6373 -1.9; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul Jet Pro ANC On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Jet Pro ANC On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 66 Hz   | 0.15 | -6.2 dB  |
| Peaking | 418 Hz  | 0.84 | -13.7 dB |
| Peaking | 633 Hz  | 1.15 | 16.7 dB  |
| Peaking | 2065 Hz | 1.77 | -17.1 dB |
| Peaking | 4384 Hz | 5.88 | -9.6 dB  |
| Peaking | 33 Hz   | 3.82 | -2.3 dB  |
| Peaking | 2564 Hz | 4.74 | -1.6 dB  |
| Peaking | 3259 Hz | 6.51 | 2.0 dB   |
| Peaking | 5005 Hz | 5.42 | -2.6 dB  |
| Peaking | 6475 Hz | 4.16 | 5.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -10.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -16.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Jet%20Pro%20ANC%20On/Soul%20Jet%20Pro%20ANC%20On.png)