# Spider Moonlight
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.0; 25 -4.4; 28 -4.9; 31 -5.4; 34 -5.8; 37 -6.1; 41 -6.4; 45 -6.7; 49 -7.0; 54 -7.3; 60 -7.6; 66 -7.9; 72 -8.1; 79 -8.4; 87 -9.0; 96 -9.0; 106 -9.2; 116 -9.7; 128 -10.2; 141 -10.6; 155 -10.9; 170 -10.2; 187 -10.7; 206 -10.4; 227 -9.6; 249 -8.7; 274 -7.1; 302 -5.3; 332 -4.2; 365 -4.0; 402 -4.6; 442 -5.3; 486 -5.8; 535 -6.0; 588 -6.2; 647 -5.7; 712 -4.8; 783 -4.7; 861 -5.2; 947 -5.5; 1042 -5.8; 1146 -6.0; 1261 -6.3; 1387 -7.2; 1526 -8.6; 1678 -9.7; 1846 -10.5; 2031 -11.3; 2234 -11.9; 2457 -11.6; 2703 -10.6; 2973 -10.5; 3270 -10.5; 3597 -9.8; 3957 -10.5; 4353 -9.9; 4788 -6.7; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -7.4; 10263 -9.4; 11289 -7.3; 12418 -8.8; 13660 -11.1; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spider Moonlight GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider Moonlight ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 2.14 | 3.0 dB  |
| Peaking | 144 Hz   | 1.35 | -4.7 dB |
| Peaking | 2198 Hz  | 2.84 | -3.6 dB |
| Peaking | 5306 Hz  | 0.66 | -8.9 dB |
| Peaking | 5870 Hz  | 1.97 | 16.0 dB |
| Peaking | 222 Hz   | 3.09 | -2.2 dB |
| Peaking | 346 Hz   | 2.61 | 3.3 dB  |
| Peaking | 886 Hz   | 1.34 | 2.0 dB  |
| Peaking | 1698 Hz  | 4.72 | -1.4 dB |
| Peaking | 13568 Hz | 4.92 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Spider%20Moonlight/Spider%20Moonlight.png)