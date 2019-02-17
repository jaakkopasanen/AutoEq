# Samsung Level On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.1; 25 -11.3; 28 -11.6; 31 -11.8; 34 -11.9; 37 -12.0; 41 -12.2; 45 -12.3; 49 -12.3; 54 -12.5; 60 -12.7; 66 -12.9; 72 -13.0; 79 -13.3; 87 -13.5; 96 -13.6; 106 -13.6; 116 -14.0; 128 -14.5; 141 -14.4; 155 -14.3; 170 -13.7; 187 -13.7; 206 -13.0; 227 -12.2; 249 -11.4; 274 -10.3; 302 -9.2; 332 -8.9; 365 -9.1; 402 -9.1; 442 -9.3; 486 -9.4; 535 -9.8; 588 -9.4; 647 -9.1; 712 -8.2; 783 -7.2; 861 -7.1; 947 -6.5; 1042 -5.8; 1146 -5.3; 1261 -5.0; 1387 -6.1; 1526 -7.1; 1678 -8.4; 1846 -9.4; 2031 -10.7; 2234 -11.6; 2457 -11.0; 2703 -9.4; 2973 -6.9; 3270 -6.0; 3597 -7.2; 3957 -7.2; 4353 -5.6; 4788 -3.4; 5267 -1.0; 5793 -0.5; 6373 -0.7; 7010 -3.6; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.54 | -4.2 dB |
| Peaking | 137 Hz   | 0.49 | -7.5 dB |
| Peaking | 2259 Hz  | 2.8  | -6.0 dB |
| Peaking | 5833 Hz  | 3.08 | 6.7 dB  |
| Peaking | 315 Hz   | 3.95 | 1.7 dB  |
| Peaking | 579 Hz   | 2.28 | -2.0 dB |
| Peaking | 1211 Hz  | 2.42 | 2.1 dB  |
| Peaking | 1721 Hz  | 4.18 | -1.2 dB |
| Peaking | 22050 Hz | 1.78 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Samsung%20Level%20On/Samsung%20Level%20On.png)