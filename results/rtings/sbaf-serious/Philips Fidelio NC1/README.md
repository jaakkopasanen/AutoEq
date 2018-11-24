# Philips Fidelio NC1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 21 -1.5; 23 -1.4; 25 -1.2; 28 -1.0; 31 -0.8; 34 -0.5; 37 -0.3; 41 -0.1; 45 0.1; 49 0.2; 54 0.3; 60 0.4; 66 0.6; 72 1.1; 79 1.6; 87 1.9; 96 1.9; 106 1.6; 116 1.2; 128 0.7; 141 0.2; 155 -0.1; 170 -0.4; 187 -0.7; 206 -1.0; 227 -1.2; 249 -1.5; 274 -1.2; 302 -0.9; 332 -0.7; 365 -0.4; 402 -0.4; 442 -0.4; 486 -0.3; 535 -0.2; 588 -0.1; 647 -0.1; 712 -0.1; 783 -0.2; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.5; 1261 0.8; 1387 -0.2; 1526 -0.9; 1678 -0.7; 1846 -1.1; 2031 -1.5; 2234 -1.8; 2457 -2.3; 2703 -3.2; 2973 -4.1; 3270 -5.0; 3597 -5.5; 3957 -6.2; 4353 -5.9; 4788 -2.7; 5267 1.0; 5793 1.0; 6373 -2.0; 7010 -0.7; 7711 0.2; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.6; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio NC1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-20**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio NC1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.28 | -1.6 dB |
| Peaking | 92 Hz    | 1.72 | 2.2 dB  |
| Peaking | 240 Hz   | 1.59 | -1.5 dB |
| Peaking | 3623 Hz  | 1.96 | -6.4 dB |
| Peaking | 18642 Hz | 3.18 | -3.0 dB |
| Peaking | 1224 Hz  | 5.56 | 1.3 dB  |
| Peaking | 3532 Hz  | 3.49 | 3.3 dB  |
| Peaking | 4875 Hz  | 1.11 | -5.0 dB |
| Peaking | 5415 Hz  | 4.25 | 7.3 dB  |
| Peaking | 7914 Hz  | 1.25 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Philips%20Fidelio%20NC1/Philips%20Fidelio%20NC1.png)