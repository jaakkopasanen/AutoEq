# Sony WH-CH700N

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 21 -6.2; 23 -6.5; 25 -6.7; 28 -7.0; 31 -7.2; 34 -7.2; 37 -7.0; 41 -6.8; 45 -6.4; 49 -6.0; 54 -5.5; 60 -4.9; 66 -4.5; 72 -4.3; 79 -4.1; 87 -4.0; 96 -4.1; 106 -4.4; 116 -4.7; 128 -4.9; 141 -4.9; 155 -4.7; 170 -4.3; 187 -4.1; 206 -4.0; 227 -4.0; 249 -3.8; 274 -3.5; 302 -3.0; 332 -2.4; 365 -1.8; 402 -1.2; 442 -0.8; 486 -0.2; 535 0.4; 588 0.5; 647 0.6; 712 0.2; 783 -0.4; 861 -0.7; 947 -0.4; 1042 0.4; 1146 0.8; 1261 0.4; 1387 -0.6; 1526 -2.3; 1678 -4.4; 1846 -6.2; 2031 -7.0; 2234 -5.7; 2457 -4.9; 2703 -5.1; 2973 -6.1; 3270 -6.7; 3597 -5.5; 3957 -2.3; 4353 1.4; 4788 -5.2; 5267 -10.9; 5793 -4.8; 6373 -0.9; 7010 1.4; 7711 0.2; 8482 -2.9; 9330 -5.0; 10263 -3.0; 11289 -0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.4; 18182 -4.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH700N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-15**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH700N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.53 | -7.0 dB  |
| Peaking | 170 Hz   | 0.88 | -4.0 dB  |
| Peaking | 2477 Hz  | 1.3  | -6.5 dB  |
| Peaking | 5266 Hz  | 7.79 | -10.6 dB |
| Peaking | 18144 Hz | 3.37 | -4.5 dB  |
| Peaking | 1219 Hz  | 3.68 | 1.3 dB   |
| Peaking | 1855 Hz  | 3.83 | -4.1 dB  |
| Peaking | 3368 Hz  | 5.6  | -4.6 dB  |
| Peaking | 3391 Hz  | 0.28 | 1.7 dB   |
| Peaking | 9352 Hz  | 4.25 | -6.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WH-CH700N/Sony%20WH-CH700N.png)