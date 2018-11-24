# Oppo PM-3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 -1.1; 23 -0.9; 25 -0.8; 28 -0.6; 31 -0.4; 34 -0.3; 37 -0.1; 41 -0.0; 45 -0.0; 49 -0.1; 54 -0.2; 60 -0.5; 66 -1.0; 72 -1.4; 79 -1.8; 87 -2.2; 96 -2.6; 106 -3.0; 116 -3.4; 128 -3.7; 141 -3.8; 155 -3.8; 170 -3.6; 187 -3.5; 206 -3.1; 227 -2.6; 249 -2.0; 274 -1.3; 302 -0.6; 332 -0.0; 365 0.2; 402 0.1; 442 -0.2; 486 -0.6; 535 -1.2; 588 -1.9; 647 -1.9; 712 -1.7; 783 -1.4; 861 -0.9; 947 -0.2; 1042 -0.1; 1146 -0.9; 1261 -1.8; 1387 -2.5; 1526 -3.3; 1678 -3.8; 1846 -4.3; 2031 -3.9; 2234 -4.5; 2457 -4.2; 2703 -3.7; 2973 -2.6; 3270 -1.2; 3597 -0.1; 3957 -0.4; 4353 -2.0; 4788 -0.1; 5267 3.1; 5793 4.6; 6373 0.4; 7010 -4.7; 7711 -6.8; 8482 -9.9; 9330 -10.4; 10263 -3.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 143 Hz   | 1.06 | -4.1 dB  |
| Peaking | 640 Hz   | 4.34 | -1.7 dB  |
| Peaking | 2068 Hz  | 1.38 | -4.6 dB  |
| Peaking | 5686 Hz  | 5.44 | 7.0 dB   |
| Peaking | 8669 Hz  | 3.06 | -11.6 dB |
| Peaking | 19 Hz    | 1.55 | -0.9 dB  |
| Peaking | 371 Hz   | 3.53 | 1.2 dB   |
| Peaking | 548 Hz   | 3.57 | -0.3 dB  |
| Peaking | 2646 Hz  | 5.65 | -0.5 dB  |
| Peaking | 11136 Hz | 6.12 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Oppo%20PM-3/Oppo%20PM-3.png)