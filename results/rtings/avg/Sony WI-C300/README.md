# Sony WI-C300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.6; 37 5.2; 41 4.6; 45 4.1; 49 3.6; 54 3.0; 60 2.1; 66 1.3; 72 0.6; 79 -0.1; 87 -0.9; 96 -1.7; 106 -2.6; 116 -3.3; 128 -4.1; 141 -4.6; 155 -5.0; 170 -5.2; 187 -5.3; 206 -5.3; 227 -5.1; 249 -4.7; 274 -4.2; 302 -3.7; 332 -3.4; 365 -3.1; 402 -2.8; 442 -2.3; 486 -1.8; 535 -1.2; 588 -0.6; 647 0.0; 712 0.6; 783 0.9; 861 0.9; 947 0.5; 1042 -0.5; 1146 -1.4; 1261 -2.2; 1387 -2.4; 1526 -2.8; 1678 -3.3; 1846 -3.6; 2031 -3.9; 2234 -3.5; 2457 -2.7; 2703 -2.5; 2973 -2.8; 3270 -3.2; 3597 -3.8; 3957 -4.4; 4353 -5.4; 4788 -5.9; 5267 -5.3; 5793 -2.8; 6373 -0.5; 7010 1.8; 7711 0.3; 8482 0.0; 9330 -0.4; 10263 -3.1; 11289 -0.3; 12418 0.0; 13660 0.0; 15026 -0.6; 16529 -2.5; 18182 -0.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-C300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-C300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.56 | 6.5 dB  |
| Peaking | 177 Hz   | 0.73 | -6.0 dB |
| Peaking | 1966 Hz  | 1.64 | -3.6 dB |
| Peaking | 4568 Hz  | 2.39 | -6.0 dB |
| Peaking | 16483 Hz | 3.45 | -2.7 dB |
| Peaking | 792 Hz   | 0.78 | -2.3 dB |
| Peaking | 793 Hz   | 1.63 | 4.3 dB  |
| Peaking | 5412 Hz  | 7    | -1.7 dB |
| Peaking | 6944 Hz  | 3.89 | 2.7 dB  |
| Peaking | 10197 Hz | 8.2  | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-C300/Sony%20WI-C300.png)