# Sony MDR-ZX770BN

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 -4.0; 23 -4.8; 25 -5.4; 28 -6.3; 31 -7.0; 34 -7.5; 37 -7.7; 41 -7.9; 45 -8.0; 49 -8.1; 54 -8.0; 60 -7.8; 66 -7.6; 72 -7.2; 79 -6.8; 87 -6.4; 96 -6.1; 106 -6.1; 116 -6.1; 128 -6.2; 141 -5.9; 155 -5.3; 170 -5.6; 187 -6.5; 206 -6.3; 227 -6.0; 249 -5.6; 274 -5.2; 302 -4.6; 332 -3.8; 365 -2.7; 402 -1.6; 442 -0.5; 486 0.5; 535 1.3; 588 1.2; 647 1.1; 712 0.7; 783 0.2; 861 0.1; 947 -0.1; 1042 -0.2; 1146 -0.5; 1261 -0.4; 1387 -0.5; 1526 -1.5; 1678 -3.4; 1846 -5.8; 2031 -7.4; 2234 -6.4; 2457 -4.6; 2703 -3.2; 2973 -2.6; 3270 0.0; 3597 4.7; 3957 -3.0; 4353 -7.9; 4788 -8.7; 5267 -5.1; 5793 0.7; 6373 2.4; 7010 1.0; 7711 -3.5; 8482 -8.6; 9330 -10.0; 10263 -7.5; 11289 -2.8; 12418 0.0; 13660 0.0; 15026 -1.7; 16529 -5.4; 18182 -4.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX770BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX770BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.43 | -8.0 dB  |
| Peaking | 223 Hz   | 1.53 | -4.6 dB  |
| Peaking | 2099 Hz  | 2.67 | -7.5 dB  |
| Peaking | 9266 Hz  | 3.4  | -11.0 dB |
| Peaking | 17249 Hz | 2.59 | -6.2 dB  |
| Peaking | 591 Hz   | 2.32 | 2.3 dB   |
| Peaking | 3592 Hz  | 6.3  | 10.1 dB  |
| Peaking | 4617 Hz  | 2.29 | -10.7 dB |
| Peaking | 6212 Hz  | 3.6  | 7.5 dB   |
| Peaking | 12906 Hz | 4.31 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-ZX770BN/Sony%20MDR-ZX770BN.png)