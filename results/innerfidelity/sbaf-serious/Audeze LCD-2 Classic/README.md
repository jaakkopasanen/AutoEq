# Audeze LCD-2 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -0.9; 25 -0.9; 28 -1.0; 31 -1.1; 34 -1.2; 37 -1.3; 41 -1.4; 45 -1.5; 49 -1.7; 54 -1.9; 60 -2.1; 66 -2.4; 72 -2.7; 79 -3.1; 87 -3.5; 96 -3.9; 106 -4.0; 116 -4.2; 128 -4.5; 141 -4.7; 155 -4.9; 170 -5.1; 187 -5.2; 206 -5.4; 227 -5.4; 249 -5.5; 274 -5.6; 302 -5.7; 332 -5.8; 365 -5.9; 402 -6.0; 442 -5.7; 486 -5.8; 535 -5.7; 588 -5.5; 647 -6.1; 712 -6.7; 783 -6.9; 861 -7.0; 947 -6.2; 1042 -6.3; 1146 -5.9; 1261 -6.1; 1387 -6.4; 1526 -7.0; 1678 -7.4; 1846 -6.2; 2031 -5.1; 2234 -5.4; 2457 -3.3; 2703 -3.0; 2973 -1.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.1; 6373 -3.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.32 | 4.9 dB  |
| Peaking | 512 Hz  | 3.39 | 0.6 dB  |
| Peaking | 1656 Hz | 4    | -2.1 dB |
| Peaking | 4029 Hz | 1.11 | 6.8 dB  |
| Peaking | 14 Hz   | 0.78 | 1.6 dB  |
| Peaking | 810 Hz  | 5.55 | -1.0 dB |
| Peaking | 4203 Hz | 3.38 | -2.2 dB |
| Peaking | 5184 Hz | 1.19 | 2.1 dB  |
| Peaking | 8326 Hz | 1.6  | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)