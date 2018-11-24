# Sony MDR-7520

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.7; 28 -1.4; 31 -2.0; 34 -2.5; 37 -2.9; 41 -3.3; 45 -3.6; 49 -3.9; 54 -4.3; 60 -4.7; 66 -5.3; 72 -5.7; 79 -6.2; 87 -6.6; 96 -7.0; 106 -7.3; 116 -7.5; 128 -7.4; 141 -7.1; 155 -6.5; 170 -5.9; 187 -5.1; 206 -4.0; 227 -2.5; 249 -1.1; 274 -2.0; 302 0.4; 332 1.2; 365 0.6; 402 -0.4; 442 -1.3; 486 -1.8; 535 -1.8; 588 -1.7; 647 -1.3; 712 -1.0; 783 -0.8; 861 -0.4; 947 -0.0; 1042 -0.1; 1146 -0.4; 1261 -1.0; 1387 -1.7; 1526 -2.6; 1678 -3.7; 1846 -5.0; 2031 -5.8; 2234 -5.5; 2457 -5.5; 2703 -6.6; 2973 -7.1; 3270 -5.1; 3597 -1.6; 3957 3.2; 4353 6.0; 4788 6.0; 5267 3.3; 5793 1.1; 6373 2.8; 7010 1.9; 7711 -3.0; 8482 -10.1; 9330 -14.6; 10263 -11.7; 11289 -2.9; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -2.9; 18182 -0.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7520 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7520 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 76 Hz    | 0.79 | -5.2 dB  |
| Peaking | 140 Hz   | 1.52 | -5.0 dB  |
| Peaking | 3041 Hz  | 1.09 | -14.2 dB |
| Peaking | 4351 Hz  | 1.23 | 14.5 dB  |
| Peaking | 9403 Hz  | 3.55 | -17.6 dB |
| Peaking | 330 Hz   | 6.28 | 2.7 dB   |
| Peaking | 6983 Hz  | 4.87 | 5.6 dB   |
| Peaking | 7618 Hz  | 1.43 | -2.9 dB  |
| Peaking | 12310 Hz | 3.58 | 3.3 dB   |
| Peaking | 16859 Hz | 4.02 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20MDR-7520/Sony%20MDR-7520.png)