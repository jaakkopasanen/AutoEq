# Samsung Level On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.4; 25 -9.6; 28 -9.8; 31 -10.0; 34 -10.2; 37 -10.3; 41 -10.4; 45 -10.5; 49 -10.6; 54 -10.7; 60 -11.0; 66 -11.2; 72 -11.3; 79 -11.5; 87 -11.8; 96 -11.9; 106 -11.9; 116 -12.3; 128 -12.8; 141 -12.6; 155 -12.6; 170 -12.0; 187 -12.0; 206 -11.3; 227 -10.5; 249 -9.7; 274 -8.6; 302 -7.5; 332 -7.2; 365 -7.4; 402 -7.4; 442 -7.6; 486 -7.7; 535 -8.0; 588 -7.7; 647 -7.4; 712 -6.5; 783 -5.5; 861 -5.3; 947 -4.8; 1042 -4.1; 1146 -3.6; 1261 -3.3; 1387 -4.4; 1526 -5.4; 1678 -6.7; 1846 -7.7; 2031 -9.0; 2234 -9.9; 2457 -9.3; 2703 -7.7; 2973 -5.1; 3270 -4.3; 3597 -5.5; 3957 -5.4; 4353 -3.8; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 0.35 | -4.0 dB |
| Peaking | 154 Hz  | 1.09 | -3.9 dB |
| Peaking | 1183 Hz | 2.27 | 3.6 dB  |
| Peaking | 2216 Hz | 3.51 | -4.4 dB |
| Peaking | 5498 Hz | 2.29 | 6.7 dB  |
| Peaking | 320 Hz  | 5.24 | 1.2 dB  |
| Peaking | 555 Hz  | 3.96 | -1.2 dB |
| Peaking | 3194 Hz | 7.28 | 2.2 dB  |
| Peaking | 3850 Hz | 7.34 | -0.9 dB |
| Peaking | 8243 Hz | 4.45 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Samsung%20Level%20On/Samsung%20Level%20On.png)