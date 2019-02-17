# Shure SRH1440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.8; 79 -1.7; 87 -2.5; 96 -3.3; 106 -3.9; 116 -4.3; 128 -4.9; 141 -5.5; 155 -6.0; 170 -6.0; 187 -6.4; 206 -6.5; 227 -6.5; 249 -6.5; 274 -6.4; 302 -6.4; 332 -6.3; 365 -6.2; 402 -6.0; 442 -5.7; 486 -5.6; 535 -5.5; 588 -5.2; 647 -4.6; 712 -5.0; 783 -5.3; 861 -5.9; 947 -6.3; 1042 -6.8; 1146 -7.1; 1261 -7.7; 1387 -8.5; 1526 -9.7; 1678 -10.9; 1846 -11.8; 2031 -12.1; 2234 -12.5; 2457 -12.4; 2703 -12.2; 2973 -12.7; 3270 -12.8; 3597 -12.8; 3957 -12.3; 4353 -11.8; 4788 -10.1; 5267 -8.0; 5793 -6.4; 6373 -5.2; 7010 -5.5; 7711 -8.1; 8482 -12.0; 9330 -14.1; 10263 -11.2; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.55 | 6.8 dB  |
| Peaking | 776 Hz   | 1.22 | 2.7 dB  |
| Peaking | 3016 Hz  | 0.6  | -7.1 dB |
| Peaking | 6452 Hz  | 2.1  | 5.4 dB  |
| Peaking | 9168 Hz  | 3.79 | -7.9 dB |
| Peaking | 40 Hz    | 2.64 | -1.0 dB |
| Peaking | 70 Hz    | 2.51 | 1.4 dB  |
| Peaking | 188 Hz   | 1.37 | -1.0 dB |
| Peaking | 1264 Hz  | 6.41 | 0.8 dB  |
| Peaking | 11804 Hz | 4.98 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)