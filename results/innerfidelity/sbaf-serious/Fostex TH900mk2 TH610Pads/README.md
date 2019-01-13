# Fostex TH900mk2 TH610Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 -0.7; 23 -1.3; 25 -1.8; 28 -2.4; 31 -2.8; 34 -3.0; 37 -3.2; 41 -3.4; 45 -3.5; 49 -3.6; 54 -3.7; 60 -3.8; 66 -3.9; 72 -4.0; 79 -4.2; 87 -4.5; 96 -4.8; 106 -4.8; 116 -4.9; 128 -5.1; 141 -5.2; 155 -5.3; 170 -4.9; 187 -5.0; 206 -5.0; 227 -4.8; 249 -4.5; 274 -4.2; 302 -3.8; 332 -3.4; 365 -2.9; 402 -2.5; 442 -1.9; 486 -1.6; 535 -1.2; 588 -0.8; 647 -0.7; 712 -0.7; 783 0.9; 861 0.1; 947 -0.1; 1042 0.1; 1146 0.5; 1261 0.6; 1387 0.3; 1526 -0.1; 1678 -0.2; 1846 0.3; 2031 1.1; 2234 1.6; 2457 3.1; 2703 4.0; 2973 3.6; 3270 2.7; 3597 2.3; 3957 2.9; 4353 3.1; 4788 3.4; 5267 4.8; 5793 3.9; 6373 1.8; 7010 1.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH900mk2 TH610Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900mk2 TH610Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 73 Hz   | 1.32 | 1.8 dB  |
| Peaking | 81 Hz   | 0.46 | -5.6 dB |
| Peaking | 245 Hz  | 0.99 | -2.6 dB |
| Peaking | 2796 Hz | 2.33 | 3.7 dB  |
| Peaking | 5254 Hz | 2.65 | 4.4 dB  |
| Peaking | 787 Hz  | 9.67 | 1.4 dB  |
| Peaking | 1228 Hz | 4.23 | 0.7 dB  |
| Peaking | 1683 Hz | 4.33 | -0.8 dB |
| Peaking | 4011 Hz | 8.86 | 0.8 dB  |
| Peaking | 8670 Hz | 2.76 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH900mk2%20TH610Pads/Fostex%20TH900mk2%20TH610Pads.png)