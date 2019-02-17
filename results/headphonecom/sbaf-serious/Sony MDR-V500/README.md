# Sony MDR-V500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.8; 116 -1.7; 128 -2.6; 141 -3.3; 155 -2.8; 170 -3.3; 187 -3.6; 206 -3.7; 227 -2.8; 249 -3.1; 274 -3.4; 302 -4.4; 332 -4.4; 365 -4.5; 402 -4.6; 442 -4.8; 486 -5.1; 535 -5.4; 588 -5.3; 647 -5.1; 712 -5.8; 783 -5.8; 861 -5.4; 947 -6.3; 1042 -6.8; 1146 -6.4; 1261 -7.4; 1387 -8.7; 1526 -9.2; 1678 -9.2; 1846 -9.4; 2031 -9.4; 2234 -9.5; 2457 -9.6; 2703 -9.5; 2973 -10.7; 3270 -10.8; 3597 -10.2; 3957 -9.9; 4353 -9.1; 4788 -7.7; 5267 -5.8; 5793 -5.5; 6373 -7.7; 7010 -5.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.6; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.27 | 5.5 dB  |
| Peaking | 208 Hz   | 0.2  | 1.8 dB  |
| Peaking | 3596 Hz  | 0.57 | -6.3 dB |
| Peaking | 5588 Hz  | 0.96 | 4.8 dB  |
| Peaking | 10219 Hz | 8.33 | -2.1 dB |
| Peaking | 42 Hz    | 2.55 | -0.3 dB |
| Peaking | 1515 Hz  | 5.77 | -1.1 dB |
| Peaking | 2685 Hz  | 3.07 | 1.5 dB  |
| Peaking | 3080 Hz  | 2.93 | -1.1 dB |
| Peaking | 22050 Hz | 1.62 | -0.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 3.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V500/Sony%20MDR-V500.png)