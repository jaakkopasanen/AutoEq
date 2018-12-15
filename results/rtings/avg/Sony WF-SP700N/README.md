# Sony WF-SP700N

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 21 -7.0; 23 -7.4; 25 -7.7; 28 -8.1; 31 -8.3; 34 -8.5; 37 -8.5; 41 -8.5; 45 -8.4; 49 -8.4; 54 -8.4; 60 -8.4; 66 -8.4; 72 -8.3; 79 -8.2; 87 -8.1; 96 -8.1; 106 -8.1; 116 -8.1; 128 -8.0; 141 -7.8; 155 -7.8; 170 -7.6; 187 -7.3; 206 -6.8; 227 -6.3; 249 -5.7; 274 -5.1; 302 -4.5; 332 -4.0; 365 -3.4; 402 -2.9; 442 -2.4; 486 -1.9; 535 -1.4; 588 -0.8; 647 -0.1; 712 0.5; 783 1.1; 861 1.2; 947 0.6; 1042 -0.5; 1146 -1.4; 1261 -2.1; 1387 -2.6; 1526 -2.8; 1678 -3.1; 1846 -3.3; 2031 -3.4; 2234 -2.7; 2457 -1.6; 2703 -0.9; 2973 -0.6; 3270 -0.5; 3597 -0.4; 3957 -0.1; 4353 0.3; 4788 1.4; 5267 2.0; 5793 0.7; 6373 -5.8; 7010 -3.3; 7711 0.3; 8482 0.0; 9330 -2.9; 10263 -9.3; 11289 -8.2; 12418 -3.3; 13660 -0.1; 15026 -0.0; 16529 -4.9; 18182 -9.7; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WF-SP700N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WF-SP700N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.29 | -8.3 dB  |
| Peaking | 188 Hz   | 0.84 | -4.1 dB  |
| Peaking | 1800 Hz  | 2.33 | -3.5 dB  |
| Peaking | 21386 Hz | 0.11 | -4.2 dB  |
| Peaking | 22195 Hz | 0.5  | -7.0 dB  |
| Peaking | 5054 Hz  | 3.4  | 5.0 dB   |
| Peaking | 8706 Hz  | 3.28 | 10.2 dB  |
| Peaking | 10462 Hz | 1.16 | -16.4 dB |
| Peaking | 13806 Hz | 0.94 | 12.2 dB  |
| Peaking | 17756 Hz | 2.45 | -6.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WF-SP700N/Sony%20WF-SP700N.png)