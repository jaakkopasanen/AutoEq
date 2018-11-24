# Sony WF-SP700N

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 -6.5; 23 -7.0; 25 -7.4; 28 -7.9; 31 -8.3; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.7; 49 -8.7; 54 -8.7; 60 -8.7; 66 -8.5; 72 -8.3; 79 -8.0; 87 -7.8; 96 -7.7; 106 -7.6; 116 -7.6; 128 -7.5; 141 -7.2; 155 -7.2; 170 -6.9; 187 -6.7; 206 -6.3; 227 -5.8; 249 -5.1; 274 -4.4; 302 -3.6; 332 -3.0; 365 -2.4; 402 -1.9; 442 -1.3; 486 -0.7; 535 -0.2; 588 0.3; 647 0.9; 712 1.4; 783 1.6; 861 1.3; 947 0.6; 1042 -0.4; 1146 -1.2; 1261 -1.9; 1387 -2.6; 1526 -3.2; 1678 -3.4; 1846 -3.2; 2031 -2.9; 2234 -2.2; 2457 -1.2; 2703 -0.1; 2973 1.0; 3270 2.1; 3597 2.8; 3957 2.3; 4353 1.6; 4788 3.0; 5267 5.0; 5793 4.6; 6373 -2.0; 7010 0.0; 7711 0.3; 8482 0.0; 9330 -2.8; 10263 -7.6; 11289 -2.9; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WF-SP700N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WF-SP700N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 45 Hz    |  0.36 | -8.8 dB |
| Peaking | 184 Hz   |  1.1  | -4.0 dB |
| Peaking | 1766 Hz  |  2.28 | -4.0 dB |
| Peaking | 4843 Hz  |  1.62 | 3.9 dB  |
| Peaking | 10336 Hz |  5.3  | -8.7 dB |
| Peaking | 747 Hz   |  2.83 | 2.5 dB  |
| Peaking | 5692 Hz  |  7.41 | 3.1 dB  |
| Peaking | 6546 Hz  | 10.07 | -5.4 dB |
| Peaking | 12146 Hz |  4.81 | 1.1 dB  |
| Peaking | 18050 Hz |  4.2  | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WF-SP700N/Sony%20WF-SP700N.png)