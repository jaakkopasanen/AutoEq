# Fostex TH610

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 -2.0; 23 -2.2; 25 -2.3; 28 -2.5; 31 -2.6; 34 -2.6; 37 -2.7; 41 -2.8; 45 -2.9; 49 -3.0; 54 -3.1; 60 -3.2; 66 -3.3; 72 -3.3; 79 -3.4; 87 -3.8; 96 -4.2; 106 -4.5; 116 -4.7; 128 -5.0; 141 -5.2; 155 -5.2; 170 -4.8; 187 -5.0; 206 -4.8; 227 -4.6; 249 -4.3; 274 -4.0; 302 -3.5; 332 -3.0; 365 -2.4; 402 -1.7; 442 -1.0; 486 -0.8; 535 -0.4; 588 0.2; 647 0.2; 712 0.2; 783 0.4; 861 0.5; 947 0.1; 1042 -0.1; 1146 -0.0; 1261 -0.0; 1387 -0.4; 1526 -0.8; 1678 -0.8; 1846 -0.2; 2031 0.9; 2234 3.2; 2457 4.5; 2703 2.2; 2973 0.8; 3270 0.7; 3597 0.4; 3957 0.2; 4353 -0.4; 4788 0.9; 5267 3.1; 5793 2.3; 6373 0.8; 7010 1.2; 7711 0.3; 8482 0.0; 9330 -2.5; 10263 -2.9; 11289 -0.2; 12418 0.0; 13660 -0.4; 15026 -0.1; 16529 0.0; 18182 0.0; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH610 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH610 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.32 | -2.6 dB |
| Peaking | 182 Hz   | 0.82 | -4.1 dB |
| Peaking | 2433 Hz  | 4.62 | 5.1 dB  |
| Peaking | 5752 Hz  | 1.8  | 4.6 dB  |
| Peaking | 6831 Hz  | 0.59 | -2.3 dB |
| Peaking | 714 Hz   | 1.84 | 1.0 dB  |
| Peaking | 1634 Hz  | 4.55 | -1.1 dB |
| Peaking | 8634 Hz  | 3.76 | 2.3 dB  |
| Peaking | 9874 Hz  | 3.42 | -4.1 dB |
| Peaking | 11473 Hz | 2.61 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH610/Fostex%20TH610.png)