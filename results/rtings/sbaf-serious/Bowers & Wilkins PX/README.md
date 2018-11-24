# Bowers & Wilkins PX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.5; 23 -3.8; 25 -4.1; 28 -4.5; 31 -4.8; 34 -5.0; 37 -5.2; 41 -5.2; 45 -5.3; 49 -5.3; 54 -5.3; 60 -5.4; 66 -5.5; 72 -5.7; 79 -5.9; 87 -6.2; 96 -6.7; 106 -7.1; 116 -7.5; 128 -7.8; 141 -7.8; 155 -7.8; 170 -7.7; 187 -7.9; 206 -8.3; 227 -9.0; 249 -9.5; 274 -9.6; 302 -9.2; 332 -8.5; 365 -7.5; 402 -6.4; 442 -5.5; 486 -4.7; 535 -4.0; 588 -3.3; 647 -2.4; 712 -1.5; 783 -0.9; 861 -0.3; 947 -0.1; 1042 -0.2; 1146 -0.9; 1261 -1.3; 1387 -1.5; 1526 -2.1; 1678 -2.6; 1846 -2.6; 2031 -3.0; 2234 -3.2; 2457 -3.2; 2703 -0.8; 2973 4.4; 3270 6.0; 3597 -2.0; 3957 -2.7; 4353 -3.0; 4788 -1.0; 5267 3.2; 5793 5.3; 6373 3.5; 7010 2.0; 7711 0.3; 8482 -2.4; 9330 -3.4; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.47 | -4.6 dB |
| Peaking | 121 Hz   | 1.13 | -3.7 dB |
| Peaking | 283 Hz   | 0.89 | -8.5 dB |
| Peaking | 5852 Hz  | 6.1  | 6.0 dB  |
| Peaking | 24000 Hz | 2.48 | 2.6 dB  |
| Peaking | 900 Hz   | 2.96 | 1.7 dB  |
| Peaking | 2356 Hz  | 1.52 | -4.6 dB |
| Peaking | 3199 Hz  | 3.94 | 11.3 dB |
| Peaking | 3801 Hz  | 3.58 | -6.0 dB |
| Peaking | 8981 Hz  | 8.59 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bowers%20&%20Wilkins%20PX/Bowers%20&%20Wilkins%20PX.png)